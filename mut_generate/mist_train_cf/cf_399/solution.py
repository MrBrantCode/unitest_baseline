"""
QUESTION:
Create a function `calculate_sum_squared` that takes a list of integers as input, removes any negative numbers, reverses the order of the remaining positive numbers, removes duplicates and sorts the list in ascending order, and returns the sum of the squared values of the positive numbers in the list.
"""

def calculate_sum_squared(lst):
    """
    This function takes a list of integers, removes any negative numbers, reverses the order of the remaining positive numbers, 
    removes duplicates, sorts the list in ascending order, and returns the sum of the squared values of the positive numbers in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of the squared values of the positive numbers in the list.
    """
    # Remove negative numbers
    lst = [num for num in lst if num >= 0]

    # Reverse order of positive numbers
    lst = lst[::-1]

    # Remove duplicates and sort in ascending order
    lst = sorted(set(lst))

    # Calculate sum of squared positive numbers
    sum_squared = sum(num ** 2 for num in lst)

    return sum_squared