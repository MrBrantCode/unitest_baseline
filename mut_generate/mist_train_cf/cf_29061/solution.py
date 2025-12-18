"""
QUESTION:
Write a function `count_unique_modules` that takes a list of strings representing module names as input, and returns a dictionary containing the count of unique module names, ignoring leading and trailing whitespaces and being case-insensitive. The function should return a dictionary with module names that appear more than once.
"""

from typing import List, Dict

def count_unique_modules(module_names: List[str]) -> Dict[str, int]:
    unique_modules = {}
    for module in module_names:
        module = module.strip().lower()  
        unique_modules[module] = unique_modules.get(module, 0) + 1  
    return {k: v for k, v in unique_modules.items() if v > 1}