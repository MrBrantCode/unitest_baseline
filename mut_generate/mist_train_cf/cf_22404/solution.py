"""
QUESTION:
Find the names of the top three users with the highest 'score' attribute from a given JSON string, and return them in a list sorted in alphabetical order.

Write a function named `find_top_three_users` that takes a JSON string `data` as input. The function should parse the JSON data, extract the names of the top three users with the highest 'score' attribute, sort these names in alphabetical order, and return them as a list. The time complexity should be O(n log n) and the space complexity should be O(n), where n is the number of users in the JSON data.
"""

import json

def find_top_three_users(data):
    users = json.loads(data)
    sorted_users = sorted(users, key=lambda user: user['score'], reverse=True)
    top_three_users = [user['name'] for user in sorted_users[:3]]
    top_three_users.sort()
    return top_three_users