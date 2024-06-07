
###
Script used to calculate the percent helicity of a structure for each frame in a trajectory. This was used to aid in the generation of the loss in helicity between app and holo states in figures 3D,    Kihn et. al., 2021
###

#!/usr/bin/env python
import numpy as np
import argparse, os, sys
from glob import glob
from copy import deepcopy
import pickle
import mdtraj as md
import os
import pandas as pd

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pdb", \
                        help="Path to topology pdb", \
                        type=str, required=True)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args
 
args = parse()

pdb = args.pdb



traj = md.load(pdb)
array = md.compute_dssp(traj, simplified=True)
array = array[0]
H_count = 0
for x in array:
    if x == 'H':
        H_count = H_count + 1
pc_helix = (H_count/len(array))*100
with open ('Percent_Helicity.txt', 'a') as f:
    f.write(str(pc_helix) + '\n')
