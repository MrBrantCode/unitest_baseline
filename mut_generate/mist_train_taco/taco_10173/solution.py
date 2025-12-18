"""
QUESTION:
Bob is a lazy man. 

He needs you to create a method that can determine how many ```letters``` and ```digits``` are in a given string.



Example:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1
"""

def count_letters_and_digits(s: str) -> int:
    """
    Counts the number of letters and digits in the given string.

    Parameters:
    s (str): The input string to be analyzed.

    Returns:
    int: The count of letters and digits in the string.
    """
    return sum(map(str.isalnum, s))