"""
QUESTION:
Write a function `extract_fold_numbers(ls)` that takes a list of command-line strings `ls` as input, where each string represents a command to execute a script with different configuration files. Extract the fold numbers from these command-line strings, which are the integer values following the pattern `fold{number}` in the configuration file paths, and return them as a list.
"""

import re

def extract_fold_numbers(ls):
    fold_numbers = []
    pattern = r"fold(\d+)"

    for command in ls:
        match = re.search(pattern, command)  
        if match:
            fold_number = int(match.group(1))  
            fold_numbers.append(fold_number)

    return fold_numbers