"""
QUESTION:
Write a function, `retrieve_first_n_in_reverse`, that takes a list and an integer `n` as input and returns the first `n` items of the list in reverse order. The function should return the last `n` elements of the list if `n` is greater than the list length. The function should not modify the original list.
"""

def retrieve_first_n_in_reverse(lst, n):
    """
    Returns the first n items of the list in reverse order.
    If n is greater than the list length, returns the last n elements of the list.
    
    Parameters:
    lst (list): The input list.
    n (int): The number of items to retrieve.
    
    Returns:
    list: The first n items of the list in reverse order.
    """
    return lst[-n:][::-1]