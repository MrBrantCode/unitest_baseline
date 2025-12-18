"""
QUESTION:
Write a function `extract_positive_integers` that takes a JSON string as input, where the JSON data is structured with a 'data' key containing a list of dictionaries with 'id' and 'value' keys. The function should extract and return all positive integers from the 'value' keys in the JSON data.
"""

import json
def extract_positive_integers(json_data):
    data = json.loads(json_data)['data']
    positive_integers = [d['value'] for d in data if isinstance(d['value'], int) and d['value'] > 0]
    return positive_integers