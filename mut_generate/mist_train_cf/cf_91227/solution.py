"""
QUESTION:
Create a function `sort_users` that takes a list of user dictionaries as input. Each dictionary contains 'name' and 'age' keys. Sort the list of users first by 'age' in descending order, and then by 'name' in ascending order.
"""

def sort_users(users):
    return sorted(users, key=lambda user: (-user['age'], user['name']))