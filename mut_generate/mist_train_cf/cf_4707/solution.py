"""
QUESTION:
Write a function called 'is_sorted' that takes an array of integers as input and checks if it is sorted in ascending order with the constraint that all even numbers come before all odd numbers. The function should also return the number of unique elements in the array. The array can contain duplicate numbers.
"""

def entrance(arr):
    """
    Checks if the array is sorted in ascending order with the constraint that all even numbers come before all odd numbers.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    tuple: A tuple containing a boolean indicating whether the array is sorted according to the given constraint and the number of unique elements in the array.
    """
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    unique_elements = set(arr)
    
    return (sorted(even_numbers) + sorted(odd_numbers) == arr), len(unique_elements)