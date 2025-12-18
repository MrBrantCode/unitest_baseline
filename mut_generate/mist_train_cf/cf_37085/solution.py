"""
QUESTION:
Implement a method `process_json_data` within a Python class that processes JSON data and updates a dictionary based on certain conditions. The method takes in a JSON string `value` and an optional `sort_key` parameter. It uses a predefined list of secondary indexes (`self._secondary_indexes`) to update the dictionary with values from the JSON object if they are not empty or None. If a `sort_key` is provided, the method performs additional processing based on this key. The method returns the updated dictionary.
"""

import json

def process_json_data(value, secondary_indexes, sort_key=None):
    obj = json.loads(value)
    item = {}
    for index in secondary_indexes:
        if obj.get(index, None) not in ['', None]:
            item.update({
                index: obj[index]
            })
    if sort_key is not None:
        if sort_key in item:
            item = dict(sorted(item.items(), key=lambda x: x[1]))
    return item