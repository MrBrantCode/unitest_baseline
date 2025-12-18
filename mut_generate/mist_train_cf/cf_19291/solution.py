"""
QUESTION:
Write a function `filter_list` that takes a list as input and returns the sum of all remaining integers after applying the following operations: remove all non-integer elements at even indices, remove strings containing vowels, and round floats to the nearest integer and remove if not even. The function should not take any additional arguments other than the input list.
"""

def filter_list(input_list):
    """
    This function filters a given list by removing non-integer elements at even indices, 
    strings containing vowels, and rounds floats to the nearest integer and removes if not even.
    
    Args:
    input_list (list): The input list to be filtered.
    
    Returns:
    int: The sum of remaining integers in the list.
    """
    
    # Remove elements which are not integers and have an even index
    input_list = [x for i, x in enumerate(input_list) if (i % 2 != 0 or isinstance(x, int))]
    
    # Remove strings containing vowels
    input_list = [x for x in input_list if not (isinstance(x, str) and any(c.lower() in 'aeiou' for c in x))]
    
    # Round floats to nearest integer and remove if not even
    input_list = [round(x) if isinstance(x, float) else x for x in input_list if not (isinstance(x, float) and round(x) % 2 != 0)]
    
    # Calculate the sum of remaining integers
    return sum([x for x in input_list if isinstance(x, int)])