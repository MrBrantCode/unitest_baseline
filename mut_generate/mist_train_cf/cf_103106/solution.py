"""
QUESTION:
Write a function `remove_duplicate_tuples` that takes a list of tuples as input, where each tuple consists of integers. The function should return a list of tuples with all duplicate tuples removed, while maintaining the original order.
"""

def remove_duplicate_tuples(tuples_list):
    """
    Remove duplicate tuples from a list of tuples while maintaining the original order.
    
    Args:
        tuples_list (list): A list of tuples, where each tuple consists of integers.
    
    Returns:
        list: A list of tuples with all duplicate tuples removed.
    """
    unique_tuples = []
    [unique_tuples.append(tuple) for tuple in tuples_list if tuple not in unique_tuples]
    return unique_tuples