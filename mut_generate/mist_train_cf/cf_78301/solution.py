"""
QUESTION:
Create a function named `checkUniformity` that takes a list of strings as input. The function should return 'true' if every string in the list is composed exclusively of either alphabets or numerics, and 'false' otherwise. If the input list is empty or contains non-string types, the function should return 'false'.
"""

def checkUniformity(lst):
    """
    Checks if every string in the list is composed exclusively of either alphabets or numerics.
    
    Args:
        lst (list): A list of strings.
    
    Returns:
        bool: 'true' if every string in the list is composed exclusively of either alphabets or numerics, 'false' otherwise.
    """
    if not all(isinstance(x, str) for x in lst):
        return False

    if not lst:
        return False

    is_prev_alphabetic = lst[0].isalpha()
    is_prev_numeric = lst[0].isnumeric()

    for string in lst[1:]:
        is_curr_alphabetic = string.isalpha()
        is_curr_numeric = string.isnumeric()

        if (is_curr_alphabetic, is_curr_numeric) != (is_prev_alphabetic, is_prev_numeric):
            return False

    return True