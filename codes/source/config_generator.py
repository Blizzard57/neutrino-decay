# Generates a Generic MakeConfig, which is required for the 
# Make File to Work

F = open('MakeConfig','w')
F.write('DELPHES_DIR := /home/blizzard/Research/tools/madGraph/Delphes/\n')
F.write('FASTJET_DIR := /home/blizzard/Research/tools/fastjet-install/')