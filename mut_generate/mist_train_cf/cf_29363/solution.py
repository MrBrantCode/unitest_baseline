"""
QUESTION:
Implement a function `process_raw_data` that takes a bytes object `raw_data` as input, decodes it into a string, and attempts to parse it as a JSON object. If parsing is successful, add the JSON object to the result list; otherwise, add `None`. The function should return a list of parsed JSON objects or `None` values. 

The function signature should be `def process_raw_data(raw_data: bytes) -> List[Dict[str, Any]]:`.
"""

import json
from typing import List, Dict, Any

def process_raw_data(raw_data: bytes) -> List[Dict[str, Any]]:
    result = []
    for raw in raw_data:
        try:
            decoded = raw.decode('utf-8')
            json_obj = json.loads(decoded)
            result.append(json_obj)
        except (UnicodeDecodeError, json.JSONDecodeError):
            result.append(None)
    return result