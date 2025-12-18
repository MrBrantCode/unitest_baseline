"""
QUESTION:
Write a function `find_second_largest` that takes an unsorted list of numbers as input and returns the second largest number in the list. The function should handle edge cases where the list is empty, contains less than two elements, or contains duplicate numbers. It should also handle lists with negative numbers and extremely large numbers efficiently. The function should have a time complexity of O(n) and include input validation to ensure that the input list contains only numeric values.
"""

def find_second_largest(arr):
    if arr is None or len(arr) < 2:
        return "Error: List should contain at least 2 elements."
    
    if not all(isinstance(x, (int, float)) for x in arr):
        return "Error: List should contain only numeric values."
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "Error: There is no second largest number."
    
    return second_largest