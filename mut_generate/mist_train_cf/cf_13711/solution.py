"""
QUESTION:
Write a function `retrieve_nth_element` that takes a set and an integer `n` as input, and returns the nth element of the set. Note that sets are unordered collections of unique elements, so the function should convert the set to a list or tuple before accessing the element by its index. The index is 0-based, meaning the first element is at index 0, the second element is at index 1, and so on.
"""

def retrieve_nth_element(input_set, n):
    """
    Retrieves the nth element from a given set.
    
    Args:
        input_set (set): The input set.
        n (int): The index of the element to retrieve (0-based index).
    
    Returns:
        The nth element of the set, or None if n is out of range.
    """
    my_list = list(input_set)
    if n < len(my_list):
        return my_list[n]
    else:
        return None