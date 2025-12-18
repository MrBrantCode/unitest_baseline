"""
QUESTION:
Create a function called `count_unique_items` that takes a list of elements as input, identifies the unique elements in the list, and returns the count of each unique element.
"""

from collections import Counter

def count_unique_items(lst):
    """
    Returns the count of each unique element in the input list.
    
    Parameters:
    lst (list): The input list of elements.
    
    Returns:
    dict: A dictionary where keys are the distinct elements and values are their respective counts.
    """
    counter_dict = Counter(lst)
    return counter_dict

def count_unique_items_tuple(lst):
    """
    Returns the count of each unique element in the input list as a list of tuples.
    
    Parameters:
    lst (list): The input list of elements.
    
    Returns:
    list: A list of tuples, where each tuple is the distinct entity and its count.
    """
    counter_dict = Counter(lst)
    return list(counter_dict.items())