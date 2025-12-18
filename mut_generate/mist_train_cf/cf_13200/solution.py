"""
QUESTION:
Write a function `filter_and_sort_tuples` that takes a list of tuples as input. The function should remove tuples that have a length of 3 or more and whose sum of the first two elements is greater than 8. Then, it should sort the remaining tuples in descending order based on the first element of each tuple.
"""

def filter_and_sort_tuples(data):
    """
    This function filters and sorts a list of tuples.
    
    It removes tuples that have a length of 3 or more and whose sum of the first two elements is greater than 8.
    Then, it sorts the remaining tuples in descending order based on the first element of each tuple.

    Args:
        data (list): A list of tuples.

    Returns:
        list: The filtered and sorted list of tuples.
    """
    # Remove the third element if it exists and the sum of the first two elements is greater than 8
    data = [t for t in data if len(t) < 3 or sum(t[:2]) <= 8]
    
    # Sort the list in descending order based on the first element of each tuple
    data.sort(key=lambda t: t[0], reverse=True)
    
    return data