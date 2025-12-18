"""
QUESTION:
Create a function `get_module_version` that takes a module name as input and returns its version number. The version number is found in the module's `version` attribute, and if the attribute is not found, the function should return "unknown". Additionally, the function should delete the `_key_bindings` attribute from the module. The function should handle cases where the module or attribute does not exist.
"""

import importlib

def get_module_version(module_name: str) -> str:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, 'version', 'unknown')
        if hasattr(module, '_key_bindings'): 
            del module._key_bindings
        return version
    except ImportError:
        return "unknown"