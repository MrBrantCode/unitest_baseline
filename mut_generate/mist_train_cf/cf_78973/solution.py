"""
QUESTION:
Create a function `find_user_by_username` that filters a list of user objects by their `username` attribute and returns the first matching user. If no matching user is found, the function should return `None`. The function should take in two parameters: a list of user objects and the target username to search for.
"""

def find_user_by_username(users, target_username):
    """
    Filters a list of user objects by their username attribute and returns the first matching user.
    
    Args:
        users (list): A list of user objects.
        target_username (str): The target username to search for.
    
    Returns:
        object: The first matching user object, or None if no matching user is found.
    """
    return next((user for user in users if user.username == target_username), None)