"""
QUESTION:
Create a function named `add_word` that takes a list as input. The function should recursively add the word 'excellent' to the end of the list until the list length reaches 10. However, if 'excellent' already exists in the list, the function should add 'good' instead. If the list length is already 10 or more, the function should return the list as is.
"""

def add_word(lst):
    """
    Recursively adds 'excellent' or 'good' to the end of the input list until the list length reaches 10.
    If 'excellent' already exists in the list, 'good' is added instead.
    
    Args:
        lst (list): Input list
    
    Returns:
        list: List with 'excellent' or 'good' added until length reaches 10
    """
    if len(lst) < 10:
        if 'excellent' in lst:
            lst.append('good')
        else:
            lst.append('excellent')
        return add_word(lst)
    else:
        return lst