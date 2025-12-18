"""
QUESTION:
Write a function `sort_users_by_age` that takes a JSON array of user objects as input, where each object contains `user_id`, `name`, and `age`. The function should return a CSV string with the format "user_id, name, age" containing users who are at least 18 years old and have an even age, sorted by age in ascending order, and limited to a maximum of 100 users.
"""

import json
import csv

def sort_users_by_age(users):
    # Filter and sort users by age
    filtered_users = [user for user in users if user['age'] >= 18 and user['age'] % 2 == 0]
    sorted_users = sorted(filtered_users, key=lambda user: user['age'])
    
    # Limit the sorted users to a maximum of 100
    limited_users = sorted_users[:100]
    
    # Generate CSV string
    csv_string = 'user_id, name, age\n'
    for user in limited_users:
        csv_string += f"{user['user_id']}, {user['name']}, {user['age']}\n"
    
    return csv_string.strip()  # Remove trailing newline