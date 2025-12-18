"""
QUESTION:
Create a function `count_cmdline_args` that takes a list of command-line arguments as input, ignores the first argument (script name), and returns a dictionary where the keys are the unique arguments and the values are their respective frequencies. The function should not consider the first element in the list and return the frequency of each unique argument in the rest of the list.
"""

from typing import List, Dict

def count_cmdline_args(cmdline_args: List[str]) -> Dict[str, int]:
    arg_freq = {}
    for arg in cmdline_args[1:]:  
        if arg in arg_freq:
            arg_freq[arg] += 1
        else:
            arg_freq[arg] = 1
    return arg_freq