"""
QUESTION:
Create a function `get_sorted_users` that takes a list of user dictionaries as input, where each dictionary contains the keys "name", "age", and "email". The function should return a JSON response containing the age, name, and email of all users in ascending order of age. The time complexity of the solution should not exceed O(n log n), where n is the number of users, and the space complexity should be constant, not allocating additional memory proportional to the number of users.
"""

import json

def get_sorted_users(users):
    """
    Returns a JSON response containing the age, name, and email of all users in ascending order of age.

    Args:
        users (list): A list of user dictionaries with keys "name", "age", and "email".

    Returns:
        str: A JSON response containing the sorted user data.
    """
    users.sort(key=lambda x: x['age'])
    response = [{"age": user["age"], "name": user["name"], "email": user["email"]} for user in users]
    return json.dumps(response)