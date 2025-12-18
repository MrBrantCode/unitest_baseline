"""
QUESTION:
Implement a function `categorize_security_strings(strings: List[str]) -> Dict[str, List[str]]` that takes a list of strings as input, where each string is in the format "system_feature_status". The function should return a dictionary where the keys are the "system_feature" part of the strings, and the values are lists of corresponding "status" parts.
"""

from typing import List, Dict

def categorize_security_strings(strings: List[str]) -> Dict[str, List[str]]:
    categorized_strings = {}
    
    for string in strings:
        system, status = string.rsplit('_', 1)
        system = system.strip()  # Remove any leading/trailing whitespace
        
        if system in categorized_strings:
            categorized_strings[system].append(status)
        else:
            categorized_strings[system] = [status]
    
    return categorized_strings