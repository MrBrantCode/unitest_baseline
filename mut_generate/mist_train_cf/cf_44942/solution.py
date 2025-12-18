"""
QUESTION:
Write a function named `find_most_repeated_term` that takes a list of strings as input and returns the term with the highest frequency of repetition. If there are multiple terms with the same highest frequency, return any one of them.
"""

from collections import Counter

def find_most_repeated_term(lst):
    """
    This function finds the term with the highest frequency of repetition in a given list.
    
    Args:
        lst (list): A list of strings.
    
    Returns:
        str: The term with the highest frequency of repetition.
    """
    # Use Counter to count the number of each element
    element_counter = Counter(lst)
    
    # Find the element with the maximum count
    most_repeated_term = element_counter.most_common(1)[0][0]
    
    return most_repeated_term