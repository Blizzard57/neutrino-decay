# Imports pyRoot, which requires a manual compile as defaut ROOT binary comes with a python2 support
from math import sqrt,fabs
import json
import sys
import h5py
import numpy as np
import awkward as ak
import ROOT
from ROOT import TLorentzVector

# Imports the required libDelphes, which is used to
# identify the objects in the ROOT file generated by delphes
ROOT.gSystem.Load("libDelphes.so")

class GenDataset:
    '''
    Gives methods to generate datasets from the root file made in delphes.
    This module helps in taking the required information from the ROOT file
     and dump it into a HDF5 file

    Attributes :
    ------------
    delphes_file : str
        Path to the input ROOT file

    is_rapid : bool
        Decides the definition of the rotational data

    total_events : int
        Number of Total Events

    dataset_dict : List
        A list of dictionary that stores 4-momenta and the rotational information of every event

    Methods :
    ---------
    create_arrays()
        Populates the dataset_dict from the ROOT file for further operation

    create_dataset()
        Generates the .h5 file from the dataset_dict, reuires the
        create_array function to be run before

    get_arrays()
        Accessor to get the dataset back from the .h5 file

    print_pretty()
        Prints tables for the 4-momenta and the azimuthal angle for an event
    '''
    def __init__(self,is_rapid = 0):
        '''
        Enter the required ROOT file

        Parameters :
        ------------
        is_rapid : bool
            True if the Delta R definition is to be take,
            False for absolute difference in azimuthal angle

        Returns :
        --------
        Nothing
        '''
        self.delphes_file = None
        self.h5_file = None
        self.is_rapid = is_rapid
        self.total_events = 0
        self.dataset_dict = []

    def load_from_root_file(self, delphes_file):
        self.delphes_file = delphes_file
        self.create_arrays()

    def load_from_dataset(self, h5_file):
        self.h5_file = h5_file
        self.pop_dataset()

    def create_arrays(self):
        '''
        Generate and populate the dataset_dict list. The list consists of a
        dictionary that contatins the 4-momenta and the azimuthal angle of an event.

        Parameters :
        ------------
        Nothing

        Returns :
        ---------
        Nothing
        '''
        root_file = ROOT.TChain("Delphes;1")
        root_file.Add(self.delphes_file)
        self.total_events = root_file.GetEntries()

        print("INFO : Started Filtering Particles")
        event_dict = []
        for i in range(self.total_events):
            entry = root_file.GetEntry(i)

            ep_array = []
            ez_array = []
            az_angle = [] # Azimuthal Angle
            ra_angle = [] # Rapidity
            ptl = 0
            ptj = 0
            ptg = 0
            ptt = 0

            entry_branch = root_file.Photon.GetEntries()
            for j in range(entry_branch):
                particle_array = [1,0,0,0,root_file.GetLeaf("Photon.PT").GetValue(j),
                                 root_file.GetLeaf("Photon.E").GetValue(j),0]
                ep_array.append(particle_array)

                az_angle.append(root_file.GetLeaf("Photon.Phi").GetValue(j))
                ra_angle.append(root_file.GetLeaf("Photon.Eta").GetValue(j))

                # Getting ptg for the MET
                ptg += root_file.GetLeaf("Photon.PT").GetValue(j)


            entry_branch = root_file.Jet.GetEntries()
            for j in range(entry_branch):

                Jet = TLorentzVector()
                Jet.SetPtEtaPhiM(root_file.GetLeaf("Jet.PT").GetValue(j),
                                 root_file.GetLeaf("Jet.Eta").GetValue(j),
                                 root_file.GetLeaf("Jet.Phi").GetValue(j),
                                 root_file.GetLeaf("Jet.Mass").GetValue(j))

                particle_array = [0,0,1 if int(root_file.GetLeaf("Jet.BTag").GetValue(j)) == 1 else -1,
                                 0,root_file.GetLeaf("Jet.PT").GetValue(j),Jet.Energy(),
                                 root_file.GetLeaf("Jet.Mass").GetValue(j)]
                ep_array.append(particle_array)

                az_angle.append(root_file.GetLeaf("Jet.Phi").GetValue(j))
                ra_angle.append(root_file.GetLeaf("Jet.Eta").GetValue(j))

                # Getting ptj for the MET
                ptj += root_file.GetLeaf("Jet.PT").GetValue(j)


            entry_branch = root_file.Electron.GetEntries()
            for j in range(entry_branch):
                Electron = TLorentzVector()
                Electron.SetPtEtaPhiM(root_file.GetLeaf("Electron.PT").GetValue(j),
                                      root_file.GetLeaf("Electron.Eta").GetValue(j),
                                      root_file.GetLeaf("Electron.Phi").GetValue(j),
                                      0)

                particle_array = [0,int(root_file.GetLeaf("Electron.Charge").GetValue(j)),0,0,
                                 root_file.GetLeaf("Electron.PT").GetValue(j),Electron.Energy(),0]
                ep_array.append(particle_array)

                az_angle.append(root_file.GetLeaf("Electron.Phi").GetValue(j))
                ra_angle.append(root_file.GetLeaf("Electron.Eta").GetValue(j))

                # Getting ptl for the MET
                ptl += root_file.GetLeaf("Electron.PT").GetValue(j)



            #entry_branch = root_file.MissingET.GetEntries()
            #for j in range(entry_branch):
            #    particle_array = [0,0,0,1,root_file.GetLeaf("MissingET.MET").GetValue(j),
            #                     root_file.GetLeaf("MissingET.MET").GetValue(j),0]
            #    ep_array.append(particle_array)
            #
            #    az_angle.append(root_file.GetLeaf("MissingET.Phi").GetValue(j))
            #    ra_angle.append(root_file.GetLeaf("MissingET.Eta").GetValue(j))


            entry_branch = root_file.Muon.GetEntries()
            for j in range(entry_branch):

                Muon = TLorentzVector()
                Muon.SetPtEtaPhiM(root_file.GetLeaf("Muon.PT").GetValue(j),
                                  root_file.GetLeaf("Muon.Eta").GetValue(j),
                                  root_file.GetLeaf("Muon.Phi").GetValue(j),
                                  0)

                particle_array = [0,int(root_file.GetLeaf("Muon.Charge").GetValue(j)),0,0,
                                 root_file.GetLeaf("Muon.PT").GetValue(j),Muon.Energy(),0]
                ep_array.append(particle_array)

                az_angle.append(root_file.GetLeaf("Muon.Phi").GetValue(j))
                ra_angle.append(root_file.GetLeaf("Muon.Eta").GetValue(j))

                # Getting ptl for the MET
                ptl += root_file.GetLeaf("Muon.PT").GetValue(j)

            entry_branch = root_file.Track.GetEntries()
            for j in range(entry_branch):

                # Getting ptt for the MET
                if root_file.GetLeaf("Track.PT").GetValue(j) > 0.4 and fabs(root_file.GetLeaf("Track.Eta").GetValue(j)) < 2.5:
                    ptt += root_file.GetLeaf("Track.PT").GetValue(j)

            entry_branch = root_file.MissingET.GetEntries()
            for j in range(entry_branch):

                # pT of MET = - (All the other selected particles)
                met_pt = - ptj -ptl -ptt -ptg
                particle_array = [0,0,0,1,met_pt,met_pt,0]
                ep_array.append(particle_array)

                az_angle.append(root_file.GetLeaf("MissingET.Phi").GetValue(j))
                ra_angle.append(root_file.GetLeaf("MissingET.Eta").GetValue(j))


            # Getting the Angular Angle Distance
            no_part = len(az_angle) # Number of particles in the event

            if self.is_rapid:
                for i in range(no_part):
                    temp_angle = []
                    for j in range(no_part):
                        temp_angle.append(sqrt((az_angle[i] - az_angle[j])**2 + (ra_angle[i] - ra_angle[j])**2))
                    ez_array.append(temp_angle)

            else:
                for i in range(no_part):
                    temp_angle = []
                    for j in range(no_part):
                        temp_angle.append(fabs(az_angle[i] - az_angle[j]))
                    ez_array.append(temp_angle)

            event_dict.append({"fourMomenta" : ep_array,"azimuthalAngle" : ez_array,
                              "phiList" : az_angle,"etaList" : ra_angle})

        self.dataset_dict = event_dict
        print("INFO : Done Filtering Particles")

    def create_dataset(self,output_file):
        '''
        Generate a HDF5 file from the dataset_dict list. The first conversion is to split the
        dictionary into 2 arrays, which are then converted to Awkward Arrays due to variable
        sizes of the particles in an event. For the conversion from Awkward to HDF5, the
        default method provided by Awkward is used.

        Parameters :
        ------------
        output_file : str, required
            Filepath/Filename of the output file

        Returns :
        ---------
        Nothing
        '''

        if self.dataset_dict == []:
            print('INFO : Empty Array. Nothing to Create')
            return 0

        print("INFO : Started Creating Database")

        xArray = []
        for i in range(self.total_events):
            xArray.append(self.dataset_dict[i]["fourMomenta"])

        azArray = []
        for i in range(self.total_events):
            azArray.append(self.dataset_dict[i]["azimuthalAngle"])

        eta = []
        for i in range(self.total_events):
            eta.append(self.dataset_dict[i]["etaList"])

        phi = []
        for i in range(self.total_events):
            phi.append(self.dataset_dict[i]["phiList"])

        hf = h5py.File(output_file,'w')
        partArray = hf.create_group("ParticleArray")
        azimuthalArray = hf.create_group("AzimuthalAngle")
        etaArray = hf.create_group("EtaAngle")
        phiArray = hf.create_group("PhiAngle")

        # Convert Particle Array to HDF5 Group

        print("INFO : Adding n-tuple")
        ak_array = ak.from_iter(xArray)
        form, length, container = ak.to_buffers(ak_array,container=partArray)
        partArray.attrs["form"] = form.tojson()
        partArray.attrs["length"] = json.dumps(length)
        partArray.keys()

        # Convert Azimuthal Angle Array to HDF5 Group

        print("INFO : Adding weights")
        ak_array = ak.from_iter(azArray)
        form, length, container = ak.to_buffers(ak_array,container=azimuthalArray)
        azimuthalArray.attrs["form"] = form.tojson()
        azimuthalArray.attrs["length"] = json.dumps(length)
        azimuthalArray.keys()

        print("INFO : Adding eta angle")
        ak_array = ak.from_iter(eta)
        form, length, container = ak.to_buffers(ak_array,container=etaArray)
        etaArray.attrs["form"] = form.tojson()
        etaArray.attrs["length"] = json.dumps(length)
        etaArray.keys()

        print("INFO : Adding phi angle")
        ak_array = ak.from_iter(phi)
        form, length, container = ak.to_buffers(ak_array,container=phiArray)
        phiArray.attrs["form"] = form.tojson()
        phiArray.attrs["length"] = json.dumps(length)
        phiArray.keys()

        hf.close()

        print("INFO : Done Creating Database")
        print("INFO : Database stored at " + str(output_file))

    def pop_dataset(self):
        '''
        Populate the dataset from the values stored in the h5 file given.

        Parameters :
        ------------
        None

        Returns :
        ---------
        None
        '''
        temp_part,temp_az,temp_eta,temp_phi = self.get_arrays(self.h5_file)
        for i in range(len(temp_part)):
            self.dataset_dict.append({"fourMomenta" : temp_part[i],"azimuthalAngle" : temp_az[i],
                              "phiList" : temp_phi[i],"etaList" : temp_eta[i]})

    def get_arrays(self,input_file):
        '''
        Accessor function that gives back lists from hdf5 file. Due to the various conversions from
        List --> Awkward --> HDF5 file, this function is made as to make the conversion back to list
        simple.

        Parameters :
        ------------
        input_file : str, required
            The hdf5 file with the converted list

        Returns :
        ---------
        particle_array : list
            The list that contains the 4-momenta of every particle in every event.

        az_array : list
            The list that contains the azimuthal angle of every particle in every event.
        '''

        print("INFO : Started Getting Data From File")

        hf = h5py.File(input_file,'r')
        partArray = hf.get("ParticleArray")
        azimuthalArray = hf.get("AzimuthalAngle")
        etaArray = hf.get("EtaAngle")
        phiArray = hf.get("PhiAngle")

        reconstitutedPartArray = ak.from_buffers(
            ak.forms.Form.fromjson(partArray.attrs["form"]),
            json.loads(partArray.attrs["length"]),
            {k: np.asarray(v) for k, v in partArray.items()},
        )

        reconstitutedAzAngle = ak.from_buffers(
            ak.forms.Form.fromjson(azimuthalArray.attrs["form"]),
            json.loads(azimuthalArray.attrs["length"]),
            {k: np.asarray(v) for k, v in azimuthalArray.items()},
        )

        reconstitutedEtaAngle = ak.from_buffers(
            ak.forms.Form.fromjson(etaArray.attrs["form"]),
            json.loads(etaArray.attrs["length"]),
            {k: np.asarray(v) for k, v in etaArray.items()},
        )

        reconstitutedPhiAngle = ak.from_buffers(
            ak.forms.Form.fromjson(phiArray.attrs["form"]),
            json.loads(phiArray.attrs["length"]),
            {k: np.asarray(v) for k, v in phiArray.items()},
        )

        particle_array = ak.to_list(reconstitutedPartArray)
        az_array = ak.to_list(reconstitutedAzAngle)
        eta_array = ak.to_list(reconstitutedEtaAngle)
        phi_array = ak.to_list(reconstitutedPhiAngle)

        print("INFO : Done Getting Data from File")

        return particle_array,az_array,eta_array,phi_array

    def print_pretty(self,array_type ,record_no = 0):
        '''
        Print any record of the dataset in a tabular format

        Parameters :
        ------------
        array_type : str, required
            Specify which data is to be printed. "fourMomenta" for 4-momenta
            and "azimuthalAngle" for the azimuthal angle

        record_no : int
            The event number for which the data is to be printed

        Returns :
        ---------
        Nothing
        '''

        if self.dataset_dict == []:
            self.create_arrays()

        if array_type == 'fourMomenta':
            print(" Photon | Lepton | Jet  | MET |  pt   |   E   |  mass ")
            print("------------------------------------------------------")
            for i in self.dataset_dict[record_no]["fourMomenta"]:
                print("   "+ str(i[0]) + "    |" + "   " +str('%2d' % i[1]) + "   |"
                      + "  "+str('%2d'%i[2])+"  |" + "  "+ str(i[3]) + "  |"
                      + str('%7.3f' % i[4]) + "|" + str('%7.3f' % i[5])
                      + "|" + str('%7.3f' % i[6]))

        else :
            part_no = len(self.dataset_dict[record_no]["azimuthalAngle"])
            print(" "*10 + "|")
            for i in range(part_no):
                print('%5d'%i + "     |")
            print()
            print("-----------"*(part_no+1))
            for i in range(part_no):
                print('%5d'%i + "     |")
                for j in range(part_no):
                    print('%10.5f'%self.dataset_dict[record_no]
                    ["azimuthalAngle"][i][j] + "|")
                print()


    def sanitize_data(self):
        '''
        Sanitizing the data to remove invalid events. The valid events have to
        have the following :

        - Two leading jets must be b-tagged
        - Only two isolated leptons with opposite signs in the event space
        '''
        if self.dataset_dict == []:
            self.create_arrays()

        print('INFO : Sanitizing the Data')
        temp_dict = []
        for i in self.dataset_dict:

            '''
            pt_jetsb = []        # List containing b-tagged Jets
            pt_all_jets = []      # List of all the Jets

            tot_charge_lepton = 0 # Sum of the charge of the Leptons
            lepton_index = []    # Index of all the Leptons

            flag = True         # Flag that True -> Survive the Cut,
                                # False -> Does not Survive the Cut

            for momenta in i["fourMomenta"]:

                # Getting a List of Jets to
                # compute cuts on them

                # B-Tagged Jet
                if momenta[2] == 1:
                    pt_jetsb.append(momenta[4])
                    pt_all_jets.append(momenta[4])

                # Non B-Tagged Jet
                elif momenta[2] == -1:
                    pt_all_jets.append(momenta[4])

                # Getting a List of Leptons to
                # compute cuts on them

                if momenta[1] != 0:
                    tot_charge_lepton += momenta[1]
                    lepton_index.append(i["fourMomenta"].index(momenta))

            # Remove all the invalid records to save time by not computing when not required
            if not flag:
                continue

            # Record invalid is less than 2 b-tagged Jets
            if len(pt_jetsb) < 2:
                continue

            # Record invalid if the two leading momenta are not of b-tagged Jets
            pt_all_jets.sort(reverse=True)
            if pt_all_jets[0] not in pt_jetsb or pt_all_jets[1] not in pt_jetsb:
                continue

            # Getting the Index of Leading Jets
            jet_index = []
            for momenta in i["fourMomenta"]:
                for j in range(2):
                    if momenta[2] == 1 and momenta[4] == pt_all_jets[j]:
                        jet_index.append(i["fourMomenta"].index(momenta))
            '''
            # Cuts for Number of Leptons being two
            # And both having opposite charge
            lepton_index = []    # Index of all the Leptons
            jet_index = []

            for momenta in i["fourMomenta"]:
                if momenta[1] != 0:
                    lepton_index.append(i["fourMomenta"].index(momenta))

                if momenta[2] != 0:
                    jet_index.append(i["fourMomenta"].index(momenta))

            if len(lepton_index) < 1 or len(jet_index) < 1:
                continue

            temp_dict.append(i)

        self.dataset_dict = temp_dict
        self.total_events = len(temp_dict)
        print("INFO : Done Sanitizing Data")

    def baseline_cuts(self):
        '''
        Applying baseline cuts to the events. There cuts are meant to
        increase the signal significance.

        Parameters :
        ------------
        Nothing

        Returns :
        ---------
        Nothing
        '''

        if self.dataset_dict == []:
            self.create_arrays  ()

        print("INFO : Applying Baseline Cuts")
        # The dictionary where events that survive the cuts are added
        temp_dict = []

        for i in self.dataset_dict:

            pt_jetsb = []        # List containing b-tagged Jets
            pt_all_jets = []      # List of all the Jets

            tot_charge_lepton = 0 # Sum of the charge of the Leptons
            lepton_index = []    # Index of all the Leptons

            flag = True         # Flag that True -> Survive the Cut,
                                # False -> Does not Survive the Cut

            for momenta in i["fourMomenta"]:

                # Getting a List of Jets to
                # compute cuts on them

                # B-Tagged Jet
                if momenta[2] == 1:
                    pt_jetsb.append(momenta[4])
                    pt_all_jets.append(momenta[4])

                # Non B-Tagged Jet
                elif momenta[2] == -1:
                    pt_all_jets.append(momenta[4])

                # Getting a List of Leptons to
                # compute cuts on them

                if momenta[1] != 0:
                    tot_charge_lepton += momenta[1]
                    lepton_index.append(i["fourMomenta"].index(momenta))

                    # PT of any Lepton has to be greater than 20 GeV
                    if momenta[4] <= 20:
                        flag = False

                # Modulus of ETmiss > 20
                if momenta[3] == 1:
                    if fabs(momenta[4]) <= 20:
                        flag = False

            # Remove all the invalid records to save time by not computing when not required
            if not flag:
                continue

            # Record invalid is less than 2 b-tagged Jets
            if len(pt_jetsb) < 2:
                continue

            # Record invalid if the two leading momenta are not of b-tagged Jets
            pt_all_jets.sort(reverse=True)
            if pt_all_jets[0] not in pt_jetsb or pt_all_jets[1] not in pt_jetsb or pt_all_jets[1] < 30:
                continue

            # Getting the Index of Leading Jets
            jet_index = []
            for momenta in i["fourMomenta"]:
                for j in range(2):
                    if momenta[2] == 1 and momenta[4] == pt_all_jets[j]:
                        jet_index.append(i["fourMomenta"].index(momenta))

            # Delta R_{bb} < 1.3 Cut
            if i['azimuthalAngle'][jet_index[0]][jet_index[1]] >= 1.3:
                flag = False

            # Mass Invariant Cut (95 GeV < M_{bb} < 140 GeV)
            jet1 = TLorentzVector()
            jet2 = TLorentzVector()

            jet1.SetPtEtaPhiM(i['fourMomenta'][jet_index[0]][4],
                              i['etaList'][jet_index[0]],
                              i['phiList'][jet_index[0]],
                              i['fourMomenta'][jet_index[0]][-1])

            jet2.SetPtEtaPhiM(i['fourMomenta'][jet_index[1]][4],
                              i['etaList'][jet_index[1]],
                              i['phiList'][jet_index[1]],
                              i['fourMomenta'][jet_index[1]][-1])

            if (jet1 + jet2).M() >= 140 or (jet1 + jet2).M() <= 95:
                flag = False

            # Cuts for Number of Leptons being two
            # And both having opposite charge
            if len(lepton_index) < 1:
                continue

            # Delta R_{ll} < 1.0 is the cut applied
            if i['azimuthalAngle'][lepton_index[0]][lepton_index[1]] >= 1.0:
                flag = False

            # The Mass Invariance Cut (M_{ll} < 65 GeV)
            lepton1 = TLorentzVector()
            lepton2 = TLorentzVector()

            lepton1.SetPtEtaPhiM(i['fourMomenta'][lepton_index[0]][4],
                                 i['etaList'][lepton_index[0]],
                                 i['phiList'][lepton_index[0]],
                                 i['fourMomenta'][lepton_index[0]][-1])

            lepton2.SetPtEtaPhiM(i['fourMomenta'][lepton_index[1]][4],
                                 i['etaList'][lepton_index[1]],
                                 i['phiList'][lepton_index[1]],
                                 i['fourMomenta'][lepton_index[1]][-1])

            if (lepton1 + lepton2).M() >= 65:
                flag = False

            if not flag:
                continue

            temp_dict.append(i)

        self.dataset_dict = temp_dict
        self.total_events = len(temp_dict)
        print("INFO : Done Applying Baseline Cuts")


if __name__ == "__main__":
    #process  = ['hh']#['ttbar','llbj','tWj','ttV','ttbarh','taubb','hh']
    #for i in process:
    #i = sys.argv[1]
    for i in ['n2n2','ttbar','wmp','wpwm','zzjj','zwpm']:
        for j in range(2,7):
            print("INFO : The process running is : " + i + ' with process number : ' + str(j))
            s1 = GenDataset()
            #s1.load_from_root_file('/home/student03/higgsSelfCoupling/results/bbWW/' + i + '_5M/Events/run_01/tag_1_delphes_events.root')
            #s1.create_dataset('/home/student03/higgsSelfCoupling/datasets/parton/'+i+'_5M.h5')
            #print("INFO : The amount of events generated are : " + str(len(s1.dataset_dict)))
            s1.load_from_dataset('/home/student03/neutrinoDecay/datasets/events/' + i + '_100k_' + str(j) +'.h5')
            s1.sanitize_data()
            s1.create_dataset('/home/student03/neutrinoDecay/datasets/sanitize/'+i+'_100k_'+ str(j) +'.h5')
            #print("INFO : The amount of events after sanitization are : " + str(len(s1.dataset_dict)))
            #s1.baseline_cuts()
            #s1.create_dataset('/home/student03/higgsSelfCoupling/datasets/baseline/'+i+'_5M.h5')
            print("INFO : The amount of events that survived are " + str(len(s1.dataset_dict)))
