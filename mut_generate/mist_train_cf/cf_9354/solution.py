"""
QUESTION:
Construct a function `construct_dict` that takes a list of lowercase English letters as input and returns a dictionary. The dictionary should have keys ranging from 1 to 10 (inclusive). The values of the dictionary should be the corresponding letters from the input list. If the list has less than 10 letters, the remaining keys should have the value 'z'.
"""

def construct_dict(letters):
    """
    Construct a dictionary with keys from 1 to 10 and values from the input list.
    If the list has less than 10 letters, the remaining keys have the value 'z'.

    Args:
        letters (list): A list of lowercase English letters.

    Returns:
        dict: A dictionary with keys from 1 to 10 and values from the input list.
    """
    return {i: letters[i-1] if i <= len(letters) else 'z' for i in range(1, 11)}