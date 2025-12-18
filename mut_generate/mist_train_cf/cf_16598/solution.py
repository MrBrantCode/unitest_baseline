"""
QUESTION:
Write a function `filter_and_multiply` that takes a list of integers and an integer as input. Filter out any value that is greater than the given number and less than or equal to 10, multiply each filtered value by 2, and return the final filtered list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def filter_and_multiply(lst, num):
    """
    Filters out any value in the list that is greater than the given number and less than or equal to 10,
    multiplies each filtered value by 2, and returns the final filtered list.

    Args:
        lst (list): A list of integers.
        num (int): An integer to compare with the list values.

    Returns:
        list: The filtered list of integers.
    """
    return [value * 2 for value in lst if value > num and value <= 10]