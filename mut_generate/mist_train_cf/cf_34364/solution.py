"""
QUESTION:
Create a function `load_modules` that takes a directory path as input and returns a list of Python module names that can be imported from that directory and its subdirectories. The function should prioritize modules in the root directory over those in subdirectories. The directory path is expected to contain Python files with a `.py` extension, and the function should extract the module names from the file names by removing the extension.
"""

import os

def load_modules(directory_path):
    """
    Returns a list of Python module names that can be imported from the given directory and its subdirectories.
    
    The function prioritizes modules in the root directory over those in subdirectories.
    
    Parameters:
    directory_path (str): The path to the directory containing Python modules.
    
    Returns:
    list: A list of Python module names.
    """
    module_names = set()
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                module_name, _ = os.path.splitext(file)
                if root == directory_path:
                    module_names = {module_name} | module_names
                else:
                    module_names.add(module_name)
    return list(module_names)