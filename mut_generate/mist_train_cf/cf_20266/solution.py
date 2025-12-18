"""
QUESTION:
Create a function `count_and_sum_elements` that takes two parameters: an array of numbers and a value `x`. If the array is empty or `x` is not provided, the function should return 0. Otherwise, it should return a tuple containing the count of elements in the array that are larger than `x` and their sum.
"""

def count_and_sum_elements(array, x=None):
    """
    Returns a tuple containing the count of elements in the array that are larger than x and their sum.
    
    If the array is empty or x is not provided, returns 0.

    Args:
        array (list): A list of numbers.
        x (int, optional): The value to compare with. Defaults to None.

    Returns:
        tuple: A tuple containing the count and sum of elements larger than x.
    """
    if not array or x is None:
        return 0
    count = 0
    total = 0
    for num in array:
        if num > x:
            count += 1
            total += num
    return count, total