"""
QUESTION:
Implement a function `process_imports` that takes a list of import statements as strings and returns a dictionary where the keys are the module names and the values are sets of imported classes or functions. Each import statement follows the format `from <module> import (<class1>, <class2>, ...)`. If a module is imported multiple times, the function should merge the imported classes or functions into a single entry in the dictionary.

The input list of import statements is non-empty and each import statement is well-formed. The function should have the signature `process_imports(import_statements: List[str]) -> Dict[str, Set[str]]`.
"""

from typing import List, Dict, Set

def process_imports(import_statements: List[str]) -> Dict[str, Set[str]]:
    imports_dict = {}
    
    for statement in import_statements:
        module, classes = statement.split(" import ")
        module = module.split("from ")[1].strip()
        classes = classes.strip("()").split(", ")
        
        if module in imports_dict:
            imports_dict[module].update(classes)
        else:
            imports_dict[module] = set(classes)
    
    return imports_dict