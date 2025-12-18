"""
QUESTION:
Implement a function `merge_sum(arr)` that takes an array `arr` as input and returns the sum of all elements in the array. The function should use a recursive approach and not utilize any built-in sorting functions or loops. 

Additionally, implement a function `merge_even_sum(arr)` that takes an array `arr` as input and returns the sum of all even numbers in the array. The function should also use a recursive approach and not utilize any built-in sorting functions or loops.
"""

def merge_sum(arr):
    """
    This function calculates the sum of all elements in the array using a recursive approach.
    
    Parameters:
    arr (list): The input array.
    
    Returns:
    int: The sum of all elements in the array.
    """
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_sum = merge_sum(arr[:mid])
        right_sum = merge_sum(arr[mid:])
        return left_sum + right_sum


def merge_even_sum(arr):
    """
    This function calculates the sum of all even numbers in the array using a recursive approach.
    
    Parameters:
    arr (list): The input array.
    
    Returns:
    int: The sum of all even numbers in the array.
    """
    if len(arr) == 1:
        return arr[0] if arr[0] % 2 == 0 else 0
    else:
        mid = len(arr) // 2
        left_sum = merge_even_sum(arr[:mid])
        right_sum = merge_even_sum(arr[mid:])
        return left_sum + right_sum