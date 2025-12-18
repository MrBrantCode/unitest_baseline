"""
QUESTION:
Write a function named `print_json_elements(json_data)` that takes a JSON object as input and prints out its elements. The function should check for the existence of the 'name' key and print its value if it exists, or 'Name not found' if it doesn't. If the 'age' key exists, the function should check if its value is an integer and print 'Invalid age' if it's not. The function should also check for the existence of the 'address' key, which is expected to be a dictionary, and print the values of 'street', 'city', and 'zip' if they exist, or 'N/A' if they don't. If the 'address' key exists but its value is not a dictionary, the function should print 'Invalid address format'. The function should handle nested objects and print their values accordingly. If the input JSON object is empty, the function should print 'No data found'.
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