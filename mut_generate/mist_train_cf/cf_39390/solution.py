"""
QUESTION:
Write a function called `available_modules` that takes a list of module names as input and returns a dictionary containing the available modules for import, where available modules are marked as `True` and unavailable modules as `False`. The function should use the `__all__` list from the current module to determine module availability. The input list may contain module names that are not present in `__all__`. 

Function Signature: `def available_modules(module_list: List[str]) -> Dict[str, bool]`
"""

from typing import List, Dict

def available_modules(module_list: List[str]) -> Dict[str, bool]:
    available_modules_dict = {module: module in __all__ for module in module_list}
    return available_modules_dict