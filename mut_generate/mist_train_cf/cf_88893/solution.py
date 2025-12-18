"""
QUESTION:
Write a function `reformat_json_strings(json_strings)` that takes a list of JSON strings as input, and returns a list of reformatted JSON strings where each string has properly indented and formatted output, and all keys are alphabetically sorted. The solution should have a time complexity of O(n*m*log(m)), where n is the length of the longest input string and m is the number of input strings.
"""

import json

def reformat_json_strings(json_strings):
    reformatted_json_strings = []
    
    for json_string in json_strings:
        # Convert JSON string to dictionary
        data = json.loads(json_string)
        
        # Sort keys alphabetically
        sorted_data = dict(sorted(data.items()))
        
        # Convert dictionary back to JSON string
        reformatted_json_string = json.dumps(sorted_data, indent=4)
        
        reformatted_json_strings.append(reformatted_json_string)
    
    return reformatted_json_strings