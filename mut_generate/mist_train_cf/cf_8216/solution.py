"""
QUESTION:
Generate a JSON response containing the age, name, and email of all users, sorted in ascending order by the sum of the ASCII values of the characters in their names. The solution should have a time complexity not exceeding O(n log n), where n is the number of users, and use constant space complexity. The function should be named `generate_json_response` and take a list of user dictionaries as input.
"""

import json

def sum_ascii(name):
    return sum(ord(char) for char in name)

def generate_json_response(users):
    sorted_users = sorted(users, key=lambda user: sum_ascii(user['name']))
    response = [{'age': user['age'], 'name': user['name'], 'email': user['email']} for user in sorted_users]
    return json.dumps(response)