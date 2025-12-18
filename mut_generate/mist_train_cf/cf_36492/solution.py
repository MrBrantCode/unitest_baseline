"""
QUESTION:
Create a function `count_kernel_modules` that takes a list of kernel module names as input and returns a dictionary containing the frequency of each unique name. The keys of the dictionary should be the unique module names, and the values should be the frequency of each module name in the input list.

The function should take a list of strings as input and return a dictionary where the keys are strings and the values are integers.
"""

from typing import List, Dict

def count_kernel_modules(module_names: List[str]) -> Dict[str, int]:
    module_frequency = {}
    for module in module_names:
        if module in module_frequency:
            module_frequency[module] += 1
        else:
            module_frequency[module] = 1
    return module_frequency