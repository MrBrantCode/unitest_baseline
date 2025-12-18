"""
QUESTION:
Create a function named count_strings that takes a list of strings as input and returns the number of strings that start with the letter 'a' or 'A' and have a length greater than 5. The function should be case-insensitive when checking the starting letter.
"""

def count_strings(lst):
    """
    Counts the number of strings in a list that start with 'a' or 'A' and have a length greater than 5.
    
    Args:
        lst (list): A list of strings.
    
    Returns:
        int: The number of strings that meet the specified conditions.
    """
    return sum(1 for string in lst if string[0].lower() == 'a' and len(string) > 5)