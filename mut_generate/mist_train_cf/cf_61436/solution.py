"""
QUESTION:
Create a function named `search_users` that takes a list of strings as input and returns a list of users from the database whose names match the given strings. The returned list should be sorted by the 'age' field of the users in ascending order. The database is a nested dictionary with a 'users' key containing a list of user dictionaries, each with 'name', 'age', and 'details' keys.
"""

def search_users(search_terms, database):
    """
    Search for users in the database whose names match the given search terms.
    
    Args:
    search_terms (list): A list of strings to search for in the database.
    database (dict): A dictionary containing a 'users' key with a list of user dictionaries.
    
    Returns:
    list: A list of users whose names match the given search terms, sorted by age in ascending order.
    """
    result = [user for user in database['users'] if user['name'] in search_terms]
    result.sort(key=lambda x: x['age'])
    return result