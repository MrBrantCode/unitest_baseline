"""
QUESTION:
Create a function called `fetch_users` to fetch all the rows from a table 'Users'. The function should return rows where the user's age is greater than 24, the first name starts with 'J', the last name ends with 'n', and the email domain is either 'gmail.com' or 'yahoo.com'.
"""

def fetch_users(users):
    return [user for user in users 
            if user['age'] > 24 
            and user['first_name'].startswith('J') 
            and user['last_name'].endswith('n') 
            and ('gmail.com' in user['email'] or 'yahoo.com' in user['email'])]