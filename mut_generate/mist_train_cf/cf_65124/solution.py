"""
QUESTION:
Create a function `cycpattern_check` that takes two strings `a` and `b` as input and returns a boolean value. The function should return `True` if any rotational permutation of string `b` is a substring of string `a`, and `False` otherwise. The function should be case-insensitive, meaning it should treat 'A' and 'a' as the same character.
"""

def cycpattern_check(a, b):
    """
    Checks if any rotational permutation of string b is a substring of string a.
    
    Parameters:
    a (str): The main string.
    b (str): The string to check for rotational permutations.
    
    Returns:
    bool: True if any rotational permutation of string b is a substring of string a, False otherwise.
    """
    a = a.lower()
    b = b.lower()

    # Create all rotational permutations of b
    all_permutations = [b[i:] + b[:i] for i in range(len(b))]

    # Check if any rotational permutation of b exists in a
    for permutation in all_permutations:
        if permutation in a:
            return True
    return False