"""
QUESTION:
Implement a function `parseJSON` that takes in a JSON-like string and a list of keys to extract. The function should return a dictionary containing the extracted values for the given keys. If a key is not found in the input string, the corresponding value in the output dictionary should be set to `None`. The function must handle cases where the input string is not a valid JSON.
"""

from typing import List, Dict, Union
import json

def parseJSON(json_string: str, keys: List[str]) -> Dict[str, Union[str, int, bool, Dict[str, Union[str, int, bool]]]]:
    result = {}
    try:
        parsed_json = json.loads(json_string)
        for key in keys:
            if key in parsed_json:
                result[key] = parsed_json[key]
            else:
                result[key] = None
    except json.JSONDecodeError:
        for key in keys:
            result[key] = None
    return result