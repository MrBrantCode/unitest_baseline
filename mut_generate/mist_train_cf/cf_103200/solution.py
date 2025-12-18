"""
QUESTION:
Write a function `sort_and_sum_even_numbers` that takes a list of integers as input, sorts the list in descending order, and returns the sorted list along with the sum of all the even numbers in the list.
"""

def sort_and_sum_even_numbers(arr):
    """
    This function sorts the input list of integers in descending order and returns the sorted list along with the sum of all the even numbers in the list.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list containing the sorted list in descending order and the sum of all the even numbers.
    """
    
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Calculate the sum of all the even numbers
    even_sum = sum([num for num in arr if num % 2 == 0])
    
    return arr, even_sum