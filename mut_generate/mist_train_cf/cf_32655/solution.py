"""
QUESTION:
Create a function `extract_version` that takes a module as input and returns the version number in the format "MAJOR.MINOR.PATCH". The version information should be extracted from the module's MAJOR, MINOR, and PATCH variables. If the module does not contain these variables, the function should return "Version information not found".
"""

def extract_version(module):
    if hasattr(module, 'MAJOR') and hasattr(module, 'MINOR') and hasattr(module, 'PATCH'):
        return f"{module.MAJOR}.{module.MINOR}.{module.PATCH}"
    else:
        return "Version information not found"