"""
QUESTION:
Given a string of JSON data containing a list of user objects with 'name' and 'score' attributes, write a function `find_top_three_users(data)` that returns a list of the names of the top three users with the highest 'score' in alphabetical order. The function should achieve a time complexity of O(n log n) and a space complexity of O(n), where n is the number of users in the JSON data.
"""

import json

def find_top_three_users(data):
    users = json.loads(data)
    sorted_users = sorted(users, key=lambda user: user['score'], reverse=True)
    top_three_users = [user['name'] for user in sorted_users[:3]]
    top_three_users.sort()
    return top_three_users