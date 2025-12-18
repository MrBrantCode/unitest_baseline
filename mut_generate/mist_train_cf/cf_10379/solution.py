"""
QUESTION:
Create a function `sorted_odds` that takes a list of integers as input and returns a list of unique odd numbers in descending order. The function should not use any built-in sorting or duplicate removal functions. The input list can contain up to 1 million elements.
"""

def sorted_odds(original_list):
    """
    This function takes a list of integers as input, removes duplicates, 
    filters out even numbers, and returns the remaining unique odd numbers 
    in descending order.

    Args:
    original_list (list): A list of integers.

    Returns:
    list: A list of unique odd numbers in descending order.
    """
    odd_set = set()
    for x in original_list:
        if x % 2 != 0:
            odd_set.add(x)

    odd_list = list(odd_set)
    for i in range(len(odd_list)):
        for j in range(i + 1, len(odd_list)):
            if odd_list[i] < odd_list[j]:
                odd_list[i], odd_list[j] = odd_list[j], odd_list[i]

    return odd_list