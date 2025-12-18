"""
QUESTION:
Create a function called `sum_squares_even_numbers` that takes a list of elements as input, filters out non-integer elements, and returns a new list containing the squares of even integers that are greater than or equal to 0 and less than or equal to 10. If no such numbers exist in the input list, the function should return an empty list.
"""

def sum_squares_even_numbers(lst):
    """
    This function filters out non-integer elements from the input list, 
    squares the even integers that are greater than or equal to 0 and less than or equal to 10, 
    and returns them in a new list.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        list: A list of squares of even integers.
    """
    return [element**2 for element in lst if isinstance(element, int) and element % 2 == 0 and 0 <= element <= 10]