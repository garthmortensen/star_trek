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
import logging  # to replace print()
import re  # regex for filtering text

# automate the boring stuff 1 ed pg 221
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.debug("program start")

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

del dir_script, each_file, f, files_in, lines, dir_in

# %%

# =============================================================================
# remove blank lines and \n from script, and lowercase
# =============================================================================

no_blanks_list = []

for each_script in scripts:
    
    each_script_no_blanks = []
    
    for each_line in each_script:
        if each_line.isspace() == False:
            
            logging.debug(each_line.strip().lower())
            each_script_no_blanks.append(each_line.strip().lower())  # remove \n
    
    no_blanks_list.append(each_script_no_blanks)
    
del scripts, each_script, each_script_no_blanks, each_line

# %%

# =============================================================================
# keep only alphanumeric characters
# =============================================================================

alphanumeric_regex = re.compile(r"[a-zA-Z0-9]")

only_alphanumeric_list = []

for each_script in no_blanks_list:
    
    each_script_only_only_alphanumeric_list = []
    
    for each_line in each_script:
        
        alphanumeric_regex.findall(each_line)
        
        # logging.debug(each_line.strip())
        each_script_only_only_alphanumeric_list.append(each_line.strip())  # remove \n
    
    only_alphanumeric_list.append(each_script_only_only_alphanumeric_list)
    
del no_blanks_list, each_script, each_script_only_only_alphanumeric_list, each_line


# %%

alpha_only_list = []

for each_script in scripts:

    for each_line in each_script:
    
        # lower the article
        each_line = each_line.lower()
        
        # split by white spaces
        words = each_line.split()
    
        # remove all tokens that are not alphabetic
        words = [word for word in words if word.isalpha()]
    
        # remove words < char len 2 and > 15
        words = [word for word in words if len(word) > 2 and len(word) < 15]
        
        alpha_only_list.append(words)


# %%


sample = no_blanks_list[0][6]


alphanumeric_regex = re.compile(r"[a-zA-Z0-9 ]")  #alphanumeric and space

out = alphanumeric_regex.findall(sample)



# %%

alphanumeric_regex = re.compile(r"[a-zA-Z0-9]")

only_alphanumeric_list = []

for each_script in no_blanks_list:
    
    each_script_only_only_alphanumeric_list = []
    
    for each_line in each_script:
        
        alphanumeric_regex.findall(each_line)
        
        # logging.debug(each_line.strip())
        each_script_only_only_alphanumeric_list.append(each_line.strip())  # remove \n
    
    only_alphanumeric_list.append(each_script_only_only_alphanumeric_list)
    
del no_blanks_list, each_script, each_script_only_only_alphanumeric_list, each_line



