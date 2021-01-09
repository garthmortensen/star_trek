# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %%

# =============================================================================
# imports
# =============================================================================

import os  # for folders

# =============================================================================
# declare and set variables
# =============================================================================

# set how many scripts to read from directory
N_SCRIPTS = 2

# get path of this script's location and data folders
dir_script = os.path.dirname(__file__)
dir_in = dir_script + "\\data\\in\\"

# =============================================================================
# read scripts into list of list
# =============================================================================

# files in folder
files_in = os.listdir(dir_in)
scripts = []

# add each script to a list of list for data prep
for each_file in files_in[0:N_SCRIPTS]:  # first 2 as a sample
    print(each_file)

    with open(dir_in + each_file) as f:
        lines = f.readlines()

    scripts.append(lines)

del dir_script, each_file, f, files_in, lines

# =============================================================================
# clean the scripts
# =============================================================================



