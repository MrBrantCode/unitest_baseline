"""
QUESTION:
Create a function `construct_dictionary` that takes a list of lowercase letters as input and returns a dictionary. The dictionary should have keys ranging from 1 to 100 (inclusive) and corresponding values from the input list. If the input list is exhausted before all keys are assigned, the remaining keys should have the value 'z'.
"""

def construct_dictionary(letters):
    """
    Construct a dictionary with keys ranging from 1 to 100 (inclusive) and 
    corresponding values from the input list. If the input list is exhausted 
    before all keys are assigned, the remaining keys should have the value 'z'.

    Args:
    letters (list): A list of lowercase letters.

    Returns:
    dict: A dictionary with keys from 1 to 100 and values from the input list.
    """
    return {i: letters[i - 1] if i <= len(letters) else 'z' for i in range(1, 101)}