"""
QUESTION:
Write a function `preserve_default_values` that takes a list of dictionaries representing configuration options for a software application. Each dictionary contains key-value pairs representing a specific configuration option and may contain a key "preserve_default" with a boolean value. If "preserve_default" is True, the default value should be included in the output dictionary; otherwise, it should be omitted. If the "preserve_default" key is not present, the dictionary should be included in the output as is.

The function should return a new list of dictionaries with the default values preserved according to the "preserve_default" flag.
"""

from typing import List, Dict, Union

def preserve_default_values(config_options: List[Dict[str, Union[str, bool]]]) -> List[Dict[str, Union[str, bool]]]:
    output = []
    for option in config_options:
        if "preserve_default" in option and option["preserve_default"]:
            output.append({key: value for key, value in option.items() if key != "preserve_default"})
        else:
            output.append({key: value for key, value in option.items() if key != "preserve_default"})
    return output