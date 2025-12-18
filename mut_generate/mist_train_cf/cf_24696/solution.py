"""
QUESTION:
Create a function `unique_elements` that takes a list of mixed data types (strings and integers) as input. The function should return two separate lists, one containing unique strings and the other containing unique integers. Assume all strings are words and all integers are numbers. The input list may contain duplicate elements.
"""

def unique_elements(mixed_list):
    """
    This function takes a list of mixed data types, separates unique strings and integers, 
    and returns them as two separate lists.

    Args:
        mixed_list (list): A list containing mixed data types (strings and integers).

    Returns:
        tuple: A tuple of two lists, the first containing unique strings and the second containing unique integers.
    """

    # Separate strings and integers into different lists
    strings = [element for element in mixed_list if isinstance(element, str)]
    integers = [element for element in mixed_list if isinstance(element, int)]

    # Use set to get unique elements and convert back to list
    unique_strings = list(set(strings))
    unique_integers = list(set(integers))

    return unique_strings, unique_integers