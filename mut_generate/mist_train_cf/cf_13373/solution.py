"""
QUESTION:
Implement a Python function `authenticate_user(api_key)` that authenticates a user based on the provided `api_key`. The function should check the `api_key` against the user's credentials stored in the database and return `True` if the authentication is successful and `False` otherwise.
"""

def authenticate_user(api_key):
    """
    Authenticates a user based on the provided api_key.

    Args:
        api_key (str): The API key to be authenticated.

    Returns:
        bool: True if the authentication is successful, False otherwise.
    """
    # Replace this with your actual database query
    # For demonstration purposes, assume we have a dictionary of user credentials
    user_credentials = {
        "user1": "api_key_1",
        "user2": "api_key_2",
    }

    # Check the api_key against the user's credentials
    for user, key in user_credentials.items():
        if key == api_key:
            return True

    # If the api_key does not match any user credentials, return False
    return False