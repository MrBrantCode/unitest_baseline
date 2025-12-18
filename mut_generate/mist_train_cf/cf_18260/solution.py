"""
QUESTION:
Create a function `getNumbers(array)` that takes an array of numbers as input and returns a list of numbers that are greater than 10 and less than 100. The output list should have no duplicates and be sorted in descending order.
"""

def getNumbers(array):
    """
    Returns a list of numbers greater than 10 and less than 100 from the given array.
    The output list has no duplicates and is sorted in descending order.

    Args:
        array (list): A list of numbers.

    Returns:
        list: A list of numbers that meet the specified criteria.
    """
    result = [num for num in array if 10 < num < 100]
    return sorted(list(set(result)), reverse=True)