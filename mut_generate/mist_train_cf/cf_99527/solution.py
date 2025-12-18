"""
QUESTION:
Implement a function named `extract_positive_integers` that takes a JSON string as input and returns a list of all positive integers from the 'value' field in the JSON data. The JSON data is a dictionary with a 'data' key containing a list of dictionaries, each with 'id' and 'value' keys. The function should be able to handle large datasets with high variability in values.
"""

import json
def extract_positive_integers(json_data):
    data = json.loads(json_data)['data']
    positive_integers = [d['value'] for d in data if isinstance(d['value'], int) and d['value'] > 0]
    return positive_integers