"""
QUESTION:
Write a function `filter_elements` that takes a list as input, converts it into a tuple, removes duplicates, counts the occurrences of each element, and returns a list of elements that appear at least twice in the original list.
"""

from collections import Counter

def filter_elements(input_list):
    """
    This function takes a list, removes duplicates, counts the occurrences of each element, 
    and returns a list of elements that appear at least twice in the original list.
    
    Args:
        input_list (list): The input list to be processed.
    
    Returns:
        list: A list of elements that appear at least twice in the original list.
    """
    # Counting the elements in the list
    count_dict = Counter(input_list)
    
    # Creating the list of elements with count>=2
    return [x for x in set(input_list) if count_dict[x]>=2]