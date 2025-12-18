"""
QUESTION:
Implement a function `find_second_largest(lst)` that finds the second largest number in an unsorted list of numeric values. The function should handle lists containing less than 2 elements, negative numbers, extremely large numbers, and non-numeric values. If the input list is `None`, contains less than 2 elements, or does not have a second largest number, the function should raise an exception.
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