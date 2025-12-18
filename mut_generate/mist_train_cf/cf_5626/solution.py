"""
QUESTION:
Create a recursive function `add_list_to_nested_json` that takes a nested JSON document (`json_doc`), a target key (`target_key`), and a list (`my_list`) as input. The function should add the list to the target key in the JSON document, which is at least 4 levels deep from the root. The function should achieve this with a time complexity of O(1) by directly updating the target key without additional traversal.
"""

import json

def add_list_to_nested_json(json_doc, target_key, my_list):
    if isinstance(json_doc, dict):
        for key, value in json_doc.items():
            if key == target_key:
                json_doc[key] = my_list
                return
            add_list_to_nested_json(value, target_key, my_list)
    elif isinstance(json_doc, list):
        for item in json_doc:
            add_list_to_nested_json(item, target_key, my_list)