"""
QUESTION:
Write a function `modify_json_key` that takes a JSON string as input and returns the modified JSON object. The function should modify the value of 'key1' to be the product of 'key2' and 'key3' only if 'key3' is greater than or equal to 10. The function should handle any edge cases and potential runtime exceptions. If the keys 'key1', 'key2', or 'key3' do not exist in the JSON object, the function should not throw a KeyError.
"""

import json

def modify_json_key(json_data):
    try:
        parsed_json = json.loads(json_data)
        
        if parsed_json.get('key3', 0) >= 10:
            parsed_json['key1'] = parsed_json.get('key2', 0) * parsed_json.get('key3', 0)

        return parsed_json

    except json.JSONDecodeError:
        print('Error decoding JSON')

    except Exception as e:
        print('Unexpected Error: ', str(e))