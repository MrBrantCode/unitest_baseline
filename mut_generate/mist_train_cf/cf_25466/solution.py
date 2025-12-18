"""
QUESTION:
Create a function `sort_tuples` that sorts a list of tuples in ascending order based on the second element of each tuple. The list of tuples will be the input to this function, and the function should return the sorted list.
"""

def sort_tuples(list_of_tuples):
    """
    Sorts a list of tuples in ascending order based on the second element of each tuple.

    Args:
        list_of_tuples (list): A list of tuples.

    Returns:
        list: The sorted list of tuples.
    """
    list_of_tuples.sort(key=lambda tup: tup[1])
    return list_of_tuples