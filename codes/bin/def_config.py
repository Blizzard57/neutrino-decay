# Change it to config.py for it to work with the program
# Change the paths to the ones required

# Choices
# Complete Path : True => Absolute Path for all the packages

complete_path = False

# Constants
if complete_path:
    # (For Analysis)
    CODE_DIR = '/home/blizzard/Research/codes/bin/'            # Location of the ELF Binary
    MADGRAPH_DIR = '/home/blizzard/Research/tools/madGraph/'   # Location of MadGraph
    DATASET_DIR = '/home/blizzard/Research/datasets/csvdata/'  # Location of Storage of Dataset
    TXT_DIR = '/home/blizzard/Research/scratch/'               # Location of MadGraph Commands File
    OUTPUT_DIR = '/home/blizzard/Research/results/'            # Location of MadGraph Output
    GIT_DIR = '/home/blizzard/Projects/neutrino-decay/'        # Location of Repository

else:
    HOME_DIR = '/home/blizzard/'                           # (For Analysis)
    CODE_DIR = HOME_DIR + 'Research/codes/bin/'            # Location of the ELF Binary
    MADGRAPH_DIR = HOME_DIR + 'Research/tools/madGraph/'   # Location of MadGraph
    DATASET_DIR = HOME_DIR + 'Research/datasets/csvdata/'  # Location of Storage of Dataset
    TXT_DIR = HOME_DIR + 'Research/scratch/'               # Location of MadGraph Commands File
    OUTPUT_DIR = HOME_DIR + 'Research/results/'            # Location of MadGraph Output
    GIT_DIR = HOME_DIR + 'Projects/neutrino-decay/'        # Location of Repository

DELPHES_FILE = '/Events/run_01/tag_1_delphes_events.root'  # Location of Delphes File

RUN_MADGRAPH = True
RUN_PYTHIA = True
RUN_DELPHES = True
RUN_ANALYSIS = True

# Specific Parameters
EVENT_NAME = 'ttbar'
SIGNAL = False

# Hyper Parameters
NUM_RUNS = 1                # Number of EVENTS_NUM event runs
EVENT_NUM = int(1e4)        # Number of events to generate per run
START_SEED = 30             # The starting seed