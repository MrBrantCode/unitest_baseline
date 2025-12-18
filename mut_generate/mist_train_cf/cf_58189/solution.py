"""
QUESTION:
Find the smallest absolute value in a list of integers and return its absolute value along with all its indexes. 

Write a function named `smallest_absolute_value` that takes a list of integers as input. The function should return a tuple where the first element is the smallest absolute value and the second element is a list of all indexes of this value in the input list. Do not use built-in functions such as `min()` or `index()`.
"""

def smallest_absolute_value(lst):
    """
    This function finds the smallest absolute value in a list of integers 
    and returns its absolute value along with all its indexes.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: A tuple containing the smallest absolute value and a list of its indexes.
    """
    minimum_absolute_value = abs(lst[0])
    index_of_minimum_value = [0]

    for index, element in enumerate(lst[1:], 1):
       absolute_value = abs(element)
       if absolute_value < minimum_absolute_value:
           minimum_absolute_value = absolute_value
           index_of_minimum_value = [index]
       elif absolute_value == minimum_absolute_value:
           index_of_minimum_value.append(index)

    return (minimum_absolute_value, index_of_minimum_value)