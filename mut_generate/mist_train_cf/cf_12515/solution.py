"""
QUESTION:
Create a function named `parse_json` that takes a string of JSON data as input. The function should parse the JSON data and output it in a 3-column table. Each column should have a maximum width of 20 characters. The table should be sorted in descending order based on the length of the values in the "name" column. The function should handle nested JSON objects and arrays by displaying a blank space in the table.
"""

import json

def parse_json(json_data):
    # Parse the JSON data
    data = json.loads(json_data)

    # Initialize the table
    table = [['Name', 'Value', 'Type']]
    
    # Function to get the length of the value in the "name" column
    def get_name_length(item):
        return len(str(item['name']))

    # Function to add a row to the table
    def add_row(name, value, value_type):
        table.append([name, value, value_type])

    # Function to handle nested JSON objects and arrays
    def handle_nested(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, (dict, list)):
                    add_row(key, '', type(value).__name__)
                    handle_nested(value)
                else:
                    add_row(key, value, type(value).__name__)
        elif isinstance(item, list):
            for i, value in enumerate(item):
                if isinstance(value, (dict, list)):
                    add_row(f'[{i}]', '', type(value).__name__)
                    handle_nested(value)
                else:
                    add_row(f'[{i}]', value, type(value).__name__)

    # Iterate over the JSON data
    if isinstance(data, (dict, list)):
        handle_nested(data)
    else:
        add_row('', data, type(data).__name__)

    # Sort the table based on the length of the values in the "name" column
    table.sort(key=lambda x: len(str(x[0])) if x[0] != 'Name' else 0, reverse=True)

    # Print the table
    for row in table:
        print('{:<20}{:<20}{:<20}'.format(row[0], str(row[1])[:20], row[2]))