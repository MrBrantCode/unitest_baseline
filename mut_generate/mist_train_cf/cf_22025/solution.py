"""
QUESTION:
Write a function named `get_distinct_first_names` to return the distinct first names of all users in the database, sorted in alphabetical order. The input is a list of user dictionaries, each containing the fields `firstName`, `lastName`, `email`, and `age`. The function should return a list of strings representing the distinct first names in alphabetical order.
"""

def get_distinct_first_names(users):
    """
    Return the distinct first names of all users in the database, sorted in alphabetical order.

    Args:
        users (list): A list of user dictionaries, each containing the fields 'firstName', 'lastName', 'email', and 'age'.

    Returns:
        list: A list of strings representing the distinct first names in alphabetical order.
    """

    return sorted(set(user['firstName'] for user in users))