"""
QUESTION:
Create a function `sum_of_squares` that takes a list of integers as input and returns the sum of the squares of all elements in the list. The function should also create a dictionary where each element from the list is a key with itself as the value, and each element's square is stored as a separate value with a key in the format "element_square". The time complexity of the solution should be O(n) and the space complexity should be O(n), where n is the length of the input list.
"""

def sum_of_squares(lst):
    """
    This function calculates the sum of squares of all elements in a given list.
    It also creates a dictionary where each element from the list is a key with 
    itself as the value, and each element's square is stored as a separate value 
    with a key in the format "element_square".

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of squares of all elements in the list.
    """
    dictionary = {}
    square_sum = 0

    for element in lst:
        dictionary[element] = element
        dictionary[str(element)+'_square'] = element ** 2
        square_sum += dictionary[str(element)+'_square']

    return square_sum