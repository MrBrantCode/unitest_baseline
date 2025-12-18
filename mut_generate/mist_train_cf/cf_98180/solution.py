"""
QUESTION:
Create a function `extract_positive_integers(json_data)` that takes a JSON string as input, extracts all positive integers from the 'value' key in the 'data' list, and returns them as a list. The function should be able to handle large datasets with high variability in values.
"""

import json

def extract_positive_integers(json_data):
    data = json.loads(json_data)['data']
    positive_integers = [d['value'] for d in data if isinstance(d['value'], int) and d['value'] > 0]
    return positive_integers