"""
QUESTION:
Create a function `sum_even_squares` that takes a list of mixed data types as input and returns a new list containing the squares of the even numbers in the input list. The input list may contain positive and negative integers, as well as non-integer elements, which should be ignored. If the input list does not contain any even numbers, the function should return an empty list.
"""

def sum_even_squares(given_list):
    """
    Returns a new list containing the squares of the even numbers in the input list.
    
    Args:
        given_list (list): A list of mixed data types.
    
    Returns:
        list: A list containing the squares of the even numbers.
    """
    return [num ** 2 for num in given_list if isinstance(num, int) and num % 2 == 0]