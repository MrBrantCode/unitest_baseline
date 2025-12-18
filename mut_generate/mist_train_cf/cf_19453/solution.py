"""
QUESTION:
Write a function `check_sorted_array(arr)` to check if an array `arr` is sorted in ascending order with a specific constraint: all even numbers must come before all odd numbers. The array can contain duplicate numbers. The function should return a boolean value indicating whether the array meets this condition.
"""

def is_sorted_with_even_before_odd(arr):
    """
    Checks if the input array is sorted in ascending order with a specific constraint:
    all even numbers must come before all odd numbers.

    Args:
        arr (list): The input array to be checked.

    Returns:
        bool: True if the array meets the condition, False otherwise.
    """
    even_numbers = sorted([num for num in arr if num % 2 == 0])
    odd_numbers = sorted([num for num in arr if num % 2 != 0])
    
    return even_numbers + odd_numbers == arr