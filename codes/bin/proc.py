'''
This code creates a text file that contains code for MadGraph.
MadGraph is then run and the data is extracted and stored.
The following is implemented :
    - Combinatorix
    - Generation Level Cuts
    - Matching
'''

from distutils.util import strtobool
import os
import subprocess
import sys
from config import *

dec_wid = {'500'  : '1.588',
           '750'  : '5.460',
           '1000' : '13.02',
           '1250' : '25.51',
           '1400' : '35.87'
          }

def proc_to_gen(proc, signal = 'n2n2'):
    ret_val = ''
    if proc == 'n2n2' and signal == 'n2n2':

        # Original Decay
        ret_val += 'generate pb pb > zp > n2 n2, '
        ret_val += '(n2 > z vl~,z > j j), (n2 > w la, w > j j)\n'

        # Combinatorics on the Decay
        ret_val += 'add process pb pb > zp > n2 n2, '
        ret_val += '(n2 > w la, w > j j), (n2 > z vl~,z > j j)\n'

    elif proc == 'ttbar' and signal == 'n2n2':

        # Original Decay
        ret_val += 'generate pb pb > t t~, '
        ret_val += '(t > w+ b, w+ > l+ vl), (t~ > w- b~, w- > j j)\n'

        # Alternative Decay
        ret_val += 'add process pb pb > t t~, '
        ret_val += '(t > w+ b, w+ > j j), (t~ > w- b~, w- > l- vl~)\n'

        # Original Decay with One Jet
        ret_val += 'add process pb pb > t t~ j, '
        ret_val += '(t > w+ b, w+ > l+ vl), (t~ > w- b~, w- > j j)\n'

        # Alternative Decay with One Jet
        ret_val += 'add process pb pb > t t~ j, '
        ret_val += '(t > w+ b, w+ > j j), (t~ > w- b~, w- > l- vl~)\n'

    elif proc == 'wmp' and signal == 'n2n2':
        
        # Decay
        ret_val += 'generate pb pb > w, w > la vla\n'

        # Decay with One Jet
        ret_val += 'add process pb pb > w j, w > la vla\n'

        # Decay with Two Jets
        ret_val += 'add process pb pb > w j j, w > la vla\n'

    elif proc == 'wpwm' and signal == 'n2n2':
        
        # Decay
        ret_val += 'generate pb pb > w+ w-, w+ > l+ vl, w- > j j\n'

        ret_val += 'add process pb pb > w+ w-, w+ > j j, w- > l- vl~\n' 

        # Decay with One Jet
        ret_val += 'add process pb pb > w+ w- j, w+ > l+ vl, w- > j j\n'
        
        ret_val += 'add process pb pb > w+ w- j, w+ > j j, w- > l- vl~\n' 

        # Decay with Two Jets
        ret_val += 'add process pb pb > w+ w- j j, w+ > l+ vl, w- > j j\n'

        ret_val += 'add process pb pb > w+ w- j j, w+ > j j, w- > l- vl~\n' 

    elif proc == 'zwpm' and signal == 'n2n2':

        # Decay
        ret_val += 'generate pb pb > z w,(w > la vla), (z > j j)\n'

        # Decay with One Jet
        ret_val += 'add process pb pb > z w j,(w > la vla), (z > j j)\n'

        # Decay with Two Jets
        ret_val += 'add process pb pb > z w j j,(w > la vla), (z > j j)\n'

    return ret_val

def gen_cuts():
    ret_val = ''

    ret_val += 'set ptl      120 \n'
    ret_val += 'set ptj1min  120 \n'
    ret_val += 'set etaj     2   \n'

    return ret_val

def jet_matching(proc):
    # Reference : https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/IntroMatching
    ret_val = ''

    # Matching for ttbar at 1 Jet
    if proc == 'ttbar':
        ret_val += 'set xqcut 20\n'
        ret_val += 'set JetMatching:qCut 30\n'
        ret_val += 'set JetMatching:nJetMax 1\n'

    # Matching for W&Z at 2 Jets
    elif proc in ['wmp','wpwm','zwpm']:
        ret_val += 'set xqcut 10\n'
        ret_val += 'set JetMatching:qCut 15\n'
        ret_val += 'set JetMatching:nJetMax 2\n'

    return ret_val

def get_run_soft():
    ret_val = ''
    if RUN_PYTHIA:
        ret_val += 'shower = pythia8\n'
    else:
        ret_val += 'shower = off\n'

    if RUN_DELPHES:
        ret_val += 'detector = Delphes\n'
    else:
        ret_val += 'detector = off\n'

    if RUN_ANALYSIS:
        ret_val += 'analysis = MadAnalysis5\n'
    else:
        ret_val += 'analysis = off\n'

    return ret_val

def main(proc_name,sig_flag,gen_proc = True,mn2 = 1e3):
    # The loop starts at 1 as default seed (0) takes a random value of seed
    for i in range(START_SEED,NUM_RUNS+START_SEED):

        # Making File for MadGraph
        f = open(TXT_DIR + proc_name + '.txt','w')

        # Default Import and Variable Definitions
        if sig_flag:
                f.write('import model ' + GIT_DIR + 'model/zprhn_leptophobic_UFO\n')
        f.write('define pb = p b b~\n')
        f.write('define w = w+ w-\n')
        f.write('define la = l+ l-\n')
        f.write('define vla = vl vl~\n')

        # Generation for a Particular Channel
        f.write(proc_to_gen(proc_name))

        # General Output (Same for all the Channels)
        f.write('output ' + OUTPUT_DIR + proc_name + '\n')
        f.write('launch\n')
        f.write(get_run_soft())
        f.write('done\n')
        f.write('set nevents ' + str(EVENT_NUM) + '\n')
        f.write('set ebeam1 7000.0\nset ebeam2 7000.0\n')
        f.write(jet_matching(proc_name))
        f.write(gen_cuts())
        f.write('set iseed ' + str(i) + '\n')

        # True only for Background
        if not sig_flag:
            f.write('set cut_decays True\n')
        
        if sig_flag:
            f.write('set Mn2 ' + str(mn2) + '\n')
            f.write('set wn2 ' + dec_wid[str(mn2)] + '\n')        
        
        f.write(DELPHES_CARD)
        # Closing the file
        f.close()

        # Flag checking if process is to be generated
        if gen_proc:
            # madGraph Operations
            p = subprocess.Popen([MADGRAPH_DIR + 'bin/mg5_aMC',
                                 TXT_DIR + proc_name + '.txt'])
            p.wait()

            p = subprocess.Popen([CODE_DIR + 'dtset', 
                                  OUTPUT_DIR + proc_name + DELPHES_FILE,
                                  DATASET_DIR + proc_name + str(i) + '.csv'])
            
            p.wait()
            
            ## Deleting Garbage
            os.system('rm -rf ' + OUTPUT_DIR + proc_name)
            os.system('rm ' + TXT_DIR + proc_name + '.txt')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        proc = EVENT_NAME
        sig = SIGNAL
        mn2 = MN2   
 
    elif len(sys.argv) == 4:
        proc = sys.argv[1]
        sig = strtobool(sys.argv[2])
        mn2 = sys.argv[3]

    else:
        raise ValueError('Incorrect arguments. Format : python program.py proc_name is_signal')

    print('The process is : ',proc,' and the mass of neutrino is : ',mn2)
    main(gen_proc=RUN_MADGRAPH,proc_name = proc,sig_flag = sig,mn2 = mn2)
