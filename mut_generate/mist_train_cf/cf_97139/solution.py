"""
QUESTION:
Implement a function called `sort_users(users)` that takes a list of user dictionaries as input, where each dictionary contains 'name' and 'age' fields. The function should return the sorted list of users in alphabetical order by their name and then by their age in descending order. The time complexity of the function should not exceed O(n log n) and the space complexity should not exceed O(n).
"""

def sort_users(users):
    # Sort users by name and age
    return sorted(users, key=lambda user: (user['name'], -user['age']))