"""
QUESTION:
Create a function `print_json_elements` that takes a JSON object `json_data` as input. The function should parse the JSON object and print its elements. The function should have the following requirements:

- If the 'name' key exists in the JSON object, print its value; otherwise, print 'Name not found'.
- If the 'age' key exists in the JSON object, check if its value is an integer; if it is, print the value; otherwise, print 'Invalid age'. If the 'age' key does not exist, print 'Unknown'.
- The 'address' key should always exist in the JSON object and its value should be a dictionary. If the 'address' key exists but its value is not a dictionary, print 'Invalid address format'. If the 'address' key exists and its value is a dictionary, print the values of 'street', 'city', and 'zip' if they exist in the dictionary; otherwise, print 'N/A' for each missing value.
- The function should be able to handle nested objects in the JSON object and print their values accordingly.
- If the JSON object is empty, print 'No data found'.
"""

import json

def print_json_elements(json_data):
    if not json_data:
        print('No data found')
        return

    if 'name' in json_data:
        print('Name:', json_data['name'])
    else:
        print('Name not found')

    if 'age' in json_data:
        age = json_data['age']
        if isinstance(age, int):
            print('Age:', age)
        else:
            print('Invalid age')

    if 'address' in json_data:
        address = json_data['address']
        if isinstance(address, dict):
            print('Street:', address.get('street', 'N/A'))
            print('City:', address.get('city', 'N/A'))
            print('Zip:', address.get('zip', 'N/A'))
        else:
            print('Invalid address format')

    for key, value in json_data.items():
        if isinstance(value, dict):
            print(key.upper(), 'Object:')
            print_json_elements(value)
        else:
            print(key.upper(), 'Value:', value)