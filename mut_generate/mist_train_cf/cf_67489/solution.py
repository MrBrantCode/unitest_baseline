"""
QUESTION:
Write a function `calc` that takes two lists of tuples with a single element each and returns a list of sums of corresponding elements from the two input lists. The input lists have the same length and each tuple in the lists contains a single numeric value. The function should return a list of sums of the numeric values from corresponding tuples in the input lists.
"""

def calc(first, second):
    """
    This function calculates the sum of corresponding elements from two input lists of tuples.
    
    Args:
    first (list): The first list of tuples with a single numeric element each.
    second (list): The second list of tuples with a single numeric element each.
    
    Returns:
    list: A list of sums of the numeric values from corresponding tuples in the input lists.
    """
    return [x[0] + y[0] for x, y in zip(first, second)]