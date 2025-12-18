"""
QUESTION:
Write a function `find_second_largest` to find the second largest number in an unsorted list. The function should handle edge cases such as a list with less than 2 elements, a list with duplicate numbers, a list with negative numbers, and a list with extremely large numbers. The function should have a time complexity of O(n), handle lists with a very large number of elements efficiently, and include input validation to ensure the input list is not None and contains only numeric values. If the list contains less than 2 elements, return an error message indicating that there is no second largest number. If the list contains non-numeric values, return an error message indicating that the list should contain only numeric values.
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