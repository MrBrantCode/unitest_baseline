"""
QUESTION:
Create a function `generate_username` that takes a string `first_name` and a string `last_name` as input and returns a unique username. The username should consist of the first letter of the `first_name` followed by the entire `last_name`, all in lowercase. If the generated username already exists, a numeric suffix should be appended to make it unique. The suffix should start from 2 and increment until a unique username is found.
"""

def generate_username(first_name: str, last_name: str, existing_usernames: set) -> str:
    """
    Generate a unique username based on the first name and last name.

    Args:
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
    existing_usernames (set): A set of existing usernames.

    Returns:
    str: A unique username.
    """
    base_username = first_name[0].lower() + last_name.lower()
    username = base_username
    suffix = 2
    while username in existing_usernames:
        username = base_username + str(suffix)
        suffix += 1
    return username