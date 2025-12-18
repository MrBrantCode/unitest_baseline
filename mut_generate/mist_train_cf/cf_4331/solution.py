"""
QUESTION:
Write a function named `even_numbers` that takes an array of integers as input and returns a new array containing the even numbers from the input array in ascending order. The input array can contain between 1 and 10^6 integers, each ranging from -10^12 to 10^12.
"""

def even_numbers(arr):
    """
    Returns a new array containing the even numbers from the input array in ascending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of even integers in ascending order.
    """
    even_nums = [num for num in arr if num % 2 == 0]
    even_nums.sort()
    return even_nums