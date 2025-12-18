"""
QUESTION:
Create a function called `create_name_birthdate_dict` that takes two lists as input: `names` and `birth_dates`, both of the same length. Each name in the `names` list should be associated with the corresponding birth date in the `birth_dates` list. Return a dictionary where the keys are the names and the values are the corresponding birth dates.
"""

def create_name_birthdate_dict(names, birth_dates):
    """
    Create a dictionary where keys are names and values are corresponding birth dates.

    Args:
        names (list): A list of names.
        birth_dates (list): A list of birth dates corresponding to the names.

    Returns:
        dict: A dictionary where keys are names and values are corresponding birth dates.
    """
    return dict(zip(names, birth_dates))