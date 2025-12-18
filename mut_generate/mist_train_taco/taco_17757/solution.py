"""
QUESTION:
Failed Filter - Bug Fixing #3
Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the FilterNumber function to remove all the numbers from the string.
"""

def remove_numbers_from_string(string: str) -> str:
    """
    Removes all numeric characters from the given string.

    Parameters:
    string (str): The input string from which numbers need to be removed.

    Returns:
    str: A new string with all numeric characters removed.
    """
    return ''.join((x for x in string if not x.isdigit()))