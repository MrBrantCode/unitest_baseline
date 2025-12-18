"""
QUESTION:
Create a function `remove_non_repeat_elements` that takes a list of strings as input, removes non-repeating string elements while considering case-insensitivity, and returns the updated list. The function should be efficient for handling large datasets and should also handle special and Unicode characters.
"""

from collections import Counter

def remove_non_repeat_elements(mylist):
    """
    Removes non-repeating string elements from a list while considering case-insensitivity.

    Args:
        mylist (list): A list of strings.

    Returns:
        list: The updated list with non-repeating string elements removed.
    """
    # use Counter function of collections module to count occurrence of strings in list
    counter_obj = Counter(map(str.lower, mylist)) 

    # keep only those strings in list which occurred more than once i.e., repeating strings
    mylist = [item for item in mylist if counter_obj[str.lower(item)] > 1] 
    return mylist