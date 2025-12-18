"""
QUESTION:
Create a function named `even_squares` that takes a list of elements as input and returns a new list. The new list should contain the square of each even integer in the input list that is greater than or equal to 0 and less than or equal to 10. The function should ignore non-integer elements and return an empty list if no such even integers are found.
"""

def even_squares(given_list):
    """
    This function takes a list of elements, filters out even integers between 0 and 10 (inclusive), 
    squares them, and returns them as a new list.
    
    Args:
    given_list (list): A list of elements.
    
    Returns:
    list: A list of squares of even integers in the given list.
    """
    return [element**2 for element in given_list if isinstance(element, int) and element % 2 == 0 and 0 <= element <= 10]