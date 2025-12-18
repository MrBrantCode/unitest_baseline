"""
QUESTION:
Write a function `count_even(n)` that calculates the number of non-negative even integers less than N, where N is a non-negative integer input. The function should handle cases where N is less than 0 or a non-integer, and return an error message in such cases. Optimize the function to achieve a time complexity of O(1).
"""

def count_even(n):
    if not isinstance(n, int):
        return "Error: Input should be an integer"
    
    if n < 0:
        return "Error: Input should be non-negative integer"
    
    return (n // 2)