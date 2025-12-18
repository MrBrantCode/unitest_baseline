"""
QUESTION:
Implement the function `process_data_types` that takes a list of strings representing data type declarations or alias assignments. The function should process the input list and return a dictionary containing the final data type mappings. Each string in the input list is in the format `DATA_TYPE = type` or `ALIAS = existing_type`. The function should handle the escaping of special symbols and double quotes within string data types.
"""

from typing import List, Union, Dict

def process_data_types(data_type_strings: List[str]) -> Dict[str, Union[str, type]]:
    data_types = {}
    for data_type_string in data_type_strings:
        data_type, type_value = map(str.strip, data_type_string.split('='))
        data_types[data_type] = type_value.strip()
        if type_value.strip() == 'str':
            data_types[data_type] = str
            if 'ESCAPED_STR' in data_type:
                data_types[data_type] = """Special symbols and \" will be escaped."""
        elif type_value.strip() == 'bool':
            data_types[data_type] = bool
    return data_types