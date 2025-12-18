"""
QUESTION:
Write a function called `find_users` that retrieves all users whose age is between 16 and 18, and their first name starts with the letter "J".
"""

def find_users(users):
    return [user for user in users if 16 <= user['age'] <= 18 and user['first_name'].startswith('J')]