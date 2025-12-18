"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list containing the same elements, but with no duplicates. The original order of elements in the input list should be preserved.
"""

def remove_duplicates(input_list):
    """
    This function takes a list as input and returns a new list containing the same elements, 
    but with no duplicates. The original order of elements in the input list is preserved.

    Args:
        input_list (list): A list that may contain duplicate elements.

    Returns:
        list: A new list with duplicate elements removed.
    """

    # Method 1 - Using Set (Not preserving original order)
    # return list(set(input_list))

    # Method 2 - Using Loop (Preserving original order)
    no_duplicate = [] 
    for num in input_list: 
        if num not in no_duplicate: 
            no_duplicate.append(num) 
    return no_duplicate