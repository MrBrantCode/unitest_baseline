"""
QUESTION:
Write a function named `get_first_hobby_name` that takes a list of student dictionaries as input, where each dictionary contains a list of hobby dictionaries. The function should return the name of the first hobby from the last student's list of hobbies.
"""

def get_first_hobby_name(students):
    """
    Retrieves the name of the first hobby from the last student's list of hobbies.

    Args:
    students (list): A list of student dictionaries, each containing a list of hobby dictionaries.

    Returns:
    str: The name of the first hobby from the last student's list of hobbies.
    """
    return students[-1]["hobbies"][0]["hobbyName"]