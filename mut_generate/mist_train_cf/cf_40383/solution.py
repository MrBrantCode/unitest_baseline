"""
QUESTION:
Create a function `extract_metadata` that takes a list of strings representing package metadata as input, where each string is formatted as 'Key :: Value', and returns a dictionary containing the programming language and the required dependencies. The dictionary should have the keys 'programming_language' and 'required_dependencies' where 'programming_language' is a string and 'required_dependencies' is a list of strings. If 'Programming Language' is found, extract the last part of the value after '::'. If 'requires' or 'install_requires' is found, add the value to 'required_dependencies'.
"""

from typing import List, Dict, Union

def extract_metadata(metadata: List[str]) -> Dict[str, Union[str, List[str]]]:
    result = {'programming_language': '', 'required_dependencies': []}
    for entry in metadata:
        key, value = entry.split(' :: ')
        if key == 'Programming Language':
            result['programming_language'] = value.split(' :: ')[-1]
        elif key in ['requires', 'install_requires']:
            result['required_dependencies'].append(value)
    return result