"""
QUESTION:
Create a function called 'get_young_users' that retrieves all users who are under 19 years old and have an active account from a database table. The results should be sorted in descending order by age.
"""

def get_young_users(users):
    """
    Retrieves all users who are under 19 years old and have an active account from a database table.
    
    Args:
    users (list): A list of dictionaries representing users with 'age' and 'account_status' keys.
    
    Returns:
    list: A list of dictionaries representing users who are under 19 years old and have an active account, sorted in descending order by age.
    """
    return sorted([user for user in users if user['age'] < 19 and user['account_status'] == 'active'], key=lambda x: x['age'], reverse=True)