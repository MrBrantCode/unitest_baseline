"""
QUESTION:
Write a function `sort_tuples` that sorts a list of tuples based on their second element and in case of a tie, sorts by the first element. The list of tuples contains single character strings as the first element and integers as the second element. The function should return the sorted list of tuples. The sorting algorithm should be stable, maintaining the order of equal elements.
"""

def sort_tuples(list_of_tuples):
    """
    Sorts a list of tuples based on their second element and in case of a tie, 
    sorts by the first element.

    Args:
    list_of_tuples (list): A list of tuples containing single character strings 
                           as the first element and integers as the second element.

    Returns:
    list: The sorted list of tuples.
    """
    return sorted(list_of_tuples, key=lambda x: (x[1], str(x[0])))