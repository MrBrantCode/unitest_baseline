"""
QUESTION:
Write a Python function named `update_employee_data` that takes a JSON formatted string as input. The function should extract the nested 'employment' dictionary and 'degrees' list, calculate and display the average years worked by incrementing the 'years' key in the 'employment' dictionary by 2, add a bonus degree 'PhD' in 'Artificial Intelligence' from 'Harvard' to the 'degrees' list, and return the updated dictionary.
"""

import json

def update_employee_data(json_string):
    # parse json
    data = json.loads(json_string)

    # Extract 'employment' dictionary and 'degrees' list
    employment = data['employment']
    degrees = data['degrees']

    # Create logic that calculates and displays the average years worked
    employment['years'] += 2
    avg_years_worked = employment['years']

    # Assign a bonus degree to 'degrees' list
    bonus_degree = {"degree": "PhD", "field": "Artificial Intelligence", "University": "Harvard"}
    degrees.append(bonus_degree)

    # Add updated 'employment' dictionary and 'degrees' list back to data
    data['employment'] = employment
    data['degrees'] = degrees

    return data