"""
QUESTION:
Create a function named `filter_and_sort_users` that takes a list of dictionaries representing users with 'user_id', 'name', and 'age' keys. The function should return a CSV string containing the 'user_id', 'name', and 'age' of users who are at least 18 years old, sorted in ascending order by age.
"""

def filter_and_sort_users(users):
    filtered_users = [user for user in users if user['age'] >= 18]
    sorted_users = sorted(filtered_users, key=lambda user: user['age'])
    csv_string = 'user_id, name, age\n'
    for user in sorted_users:
        csv_string += f"{user['user_id']}, {user['name']}, {user['age']}\n"
    return csv_string