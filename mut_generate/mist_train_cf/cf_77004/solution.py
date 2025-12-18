"""
QUESTION:
Create a function named `get_unique_users` that returns a sorted list of unique user names from a given list of users. The function should also support server-side pagination based on the provided page and limit parameters. The function should take a list of user dictionaries, a page number, and a limit as input, and return a JSON response containing the paginated list of unique user names. Assume that each user dictionary has an 'id' and a 'name' key, and the page and limit parameters are non-negative integers.
"""

def get_unique_users(users, page, limit):
    """
    Returns a sorted list of unique user names from a given list of users.
    
    Supports server-side pagination based on the provided page and limit parameters.
    
    Args:
        users (list): A list of user dictionaries, each with 'id' and 'name' keys.
        page (int): The page number for pagination.
        limit (int): The number of items per page.
    
    Returns:
        list: A sorted list of unique user names.
    """
    # Extract unique names and sort them
    sorted_unique_names = sorted(set(user['name'] for user in users))
    
    # Implementing pagination
    paginated_users = sorted_unique_names[limit*(page-1): limit*page]
    
    return paginated_users