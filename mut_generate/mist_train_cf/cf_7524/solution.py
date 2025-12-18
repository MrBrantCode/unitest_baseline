"""
QUESTION:
Create a function named `sort_users_by_age` that takes a list of user dictionaries as input, where each dictionary contains 'user_id', 'name', 'age', and 'country'. The function should return a CSV string with the format "user_id, name, age" containing a maximum of 100 users who are at least 18 years old, have an even age, and reside in a country starting with the letter "A". The users should be sorted by age in ascending order.
"""

import csv

def sort_users_by_age(users):
    # Sort users by age in ascending order
    sorted_users = sorted(users, key=lambda x: x['age'])
    
    # Filter users who are at least 18 years old and have an even age
    filtered_users = filter(lambda x: x['age'] >= 18 and x['age'] % 2 == 0, sorted_users)
    
    # Filter users from countries starting with the letter "A"
    filtered_users = filter(lambda x: x['country'].startswith('A'), filtered_users)
    
    # Limit the number of users to 100
    limited_users = list(filtered_users)[:100]
    
    # Create a CSV string with the format "user_id, name, age"
    csv_string = "user_id, name, age\n"
    for user in limited_users:
        csv_string += f"{user['user_id']}, {user['name']}, {user['age']}\n"
    
    return csv_string