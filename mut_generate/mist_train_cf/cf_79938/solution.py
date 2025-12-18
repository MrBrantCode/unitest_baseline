"""
QUESTION:
Create a function named `count_unique` that takes a list of integers as input and returns a list of tuples. Each tuple contains a unique integer from the input list and its count. The tuples must be ordered based on the first occurrence of each integer in the input list. Do not use built-in functions or data structures such as set or collections. Optimize the solution for better space and time complexity.
"""

def count_unique(lst):
    """
    This function takes a list of integers as input and returns a list of tuples.
    Each tuple contains a unique integer from the input list and its count.
    The tuples must be ordered based on the first occurrence of each integer in the input list.
    
    Args:
    lst (list): A list of integers
    
    Returns:
    list: A list of tuples containing unique integers and their counts
    """
    
    count_dict = {}  # Holds unique elements as keys and their counts as values
    order = []  # Holds the order of unique elements

    for num in lst:
        if num not in count_dict:
            order.append(num)
        count_dict[num] = count_dict.get(num, 0) + 1

    return [(num, count_dict[num]) for num in order]