"""
QUESTION:
Write a function named `get_top_n_elements` that takes a list of integers and an integer `n` as input and returns the top `n` elements from the list in descending order. The function should be able to handle large lists of up to 10,000 integers. The input list is unsorted and may contain duplicate values.
"""

def get_top_n_elements(input_list, n):
    """
    This function takes a list of integers and an integer n as input, 
    and returns the top n elements from the list in descending order.

    Args:
        input_list (list): A list of integers.
        n (int): The number of top elements to return.

    Returns:
        list: A list of the top n elements from the input list in descending order.
    """
    return sorted(input_list, reverse=True)[:n]