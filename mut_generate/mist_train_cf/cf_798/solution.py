"""
QUESTION:
Write a function `find_second_largest(lst)` that finds the second largest number in an unsorted list of numbers. The function should handle lists with less than 2 elements, negative numbers, and very large numbers efficiently. It should also validate the input list to ensure it is not `None` and contains only numeric values. If no second largest number is found, the function should raise an exception.
"""

def find_second_largest(lst):
    if lst is None:
        raise Exception("Input list cannot be None")
    
    if len(lst) < 2:
        raise Exception("Input list should have at least 2 elements")
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in lst:
        if not isinstance(num, (int, float)):
            raise Exception("Input list should contain only numeric values")
        
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        raise Exception("No second largest number found")
    
    return second_largest