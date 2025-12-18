"""
QUESTION:
Write a function `string_length` that calculates the length of a given string without using the built-in `len()` function, loops, or recursion. The function must not use any string manipulation functions like `substring()` or `charAt()`.
"""

def string_length(s):
    """
    Calculate the length of a given string without using the built-in len() function, loops, or recursion.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The length of the string.
    """
    characters = list(s)
    count = 0
    try:
        while True:
            characters[count]
            count += 1
    except IndexError:
        return count