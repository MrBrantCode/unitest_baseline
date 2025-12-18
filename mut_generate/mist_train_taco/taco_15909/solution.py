"""
QUESTION:
Failed Sort - Bug Fixing #4
Oh no, Timmy's Sort doesn't seem to be working? Your task is to fix the sortArray function to sort all numbers in ascending order
"""

def sort_array(value: str) -> str:
    """
    Sorts the input string of numbers in ascending order.

    Parameters:
    value (str): A string of numbers to be sorted.

    Returns:
    str: A string of numbers sorted in ascending order.
    """
    return ''.join(sorted(value))