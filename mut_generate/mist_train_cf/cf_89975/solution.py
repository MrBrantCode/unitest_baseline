"""
QUESTION:
Write a function `sort_users_by_age(users)` that takes a list of dictionaries representing users, where each dictionary contains the keys 'user_id', 'name', 'age', and 'country'. The function should sort the users by age in ascending order, filter out users who are less than 18 years old or have an odd age, and only include users from countries starting with the letter 'A'. The output should be a CSV string with the format "user_id, name, age" and should be limited to a maximum of 100 users.
"""

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