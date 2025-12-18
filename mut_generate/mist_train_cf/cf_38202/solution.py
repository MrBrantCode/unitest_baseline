"""
QUESTION:
Create a Python function `extract_django_settings` that takes a file path to a Django settings file and a list of setting names as input, and returns a dictionary containing the specified settings and their values. If a setting is not found, its value in the dictionary should be `None`.
"""

from typing import List, Dict, Union
import importlib.util

def extract_django_settings(file_path: str, settings: List[str]) -> Dict[str, Union[str, None]]:
    extracted_settings = {}
    
    spec = importlib.util.spec_from_file_location("settings", file_path)
    settings_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings_module)
    
    for setting in settings:
        setting_value = getattr(settings_module, setting, None)
        extracted_settings[setting] = setting_value
    
    return extracted_settings