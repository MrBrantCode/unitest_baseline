"""
QUESTION:
Design a function, `generate_unique_username`, that allows users to choose their usernames while maintaining uniqueness in a single namespace system. The function should either generate a unique username internally or suggest alternative usernames by adding components to the chosen username.
"""

def generate_unique_username(chosen_username, existing_usernames):
    """
    Generates a unique username by adding a number to the chosen username if it already exists.

    Args:
        chosen_username (str): The username chosen by the user.
        existing_usernames (list): A list of existing usernames.

    Returns:
        str: A unique username.
    """
    if chosen_username not in existing_usernames:
        return chosen_username
    
    # Initialize a counter to add to the username
    counter = 1
    
    # Generate a new username by adding the counter to the chosen username
    new_username = f"{chosen_username}{counter}"
    
    # While the new username exists in the existing usernames, increment the counter and generate a new username
    while new_username in existing_usernames:
        counter += 1
        new_username = f"{chosen_username}{counter}"
    
    return new_username