"""
QUESTION:
Write a function `find_second_largest(arr)` that takes an array of integers as input and returns the second largest number in the array. The function should not use any built-in functions or methods to find the maximum or second maximum value. The time complexity of the function should be O(n) and the space complexity should be O(1). If the array has less than two elements or does not have a second largest element, the function should return a corresponding message.
"""

def find_second_largest(arr):
    """
    This function finds the second largest number in an array without using built-in functions or methods.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int or str: The second largest number in the array, or a corresponding message if the array has less than two elements or does not have a second largest element.
    """
    
    n = len(arr)
    
    if n < 2:
        return "Array should have at least two elements."
    
    largest = arr[0]
    second_largest = arr[0]
    
    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    if second_largest == largest:
        return "There is no second largest element in the array."
    else:
        return second_largest