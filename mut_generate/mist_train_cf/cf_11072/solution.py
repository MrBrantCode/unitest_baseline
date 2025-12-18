"""
QUESTION:
Implement a function named `sqrt` that calculates the square root of a given positive integer without using any built-in square root functions. The output should be rounded to the nearest integer. The algorithm should have a time complexity of O(log n).
"""

def sqrt(num):
    """
    This function calculates the square root of a given positive integer without using any built-in square root functions.
    
    Args:
    num (int): A positive integer.
    
    Returns:
    int: The square root of the given number rounded to the nearest integer.
    """
    start = 0
    end = num
    
    while start <= end:
        mid = (start + end) // 2
        
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            start = mid + 1
        else:
            end = mid - 1
            
    return end