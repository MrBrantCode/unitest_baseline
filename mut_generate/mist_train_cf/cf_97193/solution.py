"""
QUESTION:
Generate a JSON response containing the age, name, and email of all users, sorted in ascending order of age. The function should not exceed O(n log n) time complexity and constant space complexity, where n is the number of users. Implement a function called `generate_json_response` that takes a list of user dictionaries as input and returns the sorted JSON response.
"""

import json

def generate_json_response(users):
    """
    Generate a JSON response containing the age, name, and email of all users, 
    sorted in ascending order of age.

    Args:
        users (list): A list of user dictionaries.

    Returns:
        str: A JSON string containing the sorted user data.
    """
    # Sorting the users list in ascending order of age
    users.sort(key=lambda x: x['age'])

    # Creating a new list with only the required attributes
    response = [{"age": user["age"], "name": user["name"], "email": user["email"]} for user in users]

    # Converting the response list to JSON format
    return json.dumps(response)