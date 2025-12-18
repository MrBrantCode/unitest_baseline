"""
QUESTION:
Write a function `multiply_without_operator` that takes two integers as input and returns their product without using the multiplication operator (*). The function should handle negative numbers and return the correct sign for the result. Assume the input numbers will always be integers.
"""

def multiply_without_operator(num_1: int, num_2: int) -> int:
    # Check if one of the numbers is 0
    if num_1 == 0 or num_2 == 0:
        return 0
    
    # Determine the sign of the result
    sign = 1
    if num_1 < 0:
        sign = -sign
        num_1 = -num_1
    if num_2 < 0:
        sign = -sign
        num_2 = -num_2
    
    # Multiply the absolute values of the numbers
    result = 0
    for _ in range(num_1):
        result += num_2
    
    # Apply the sign to the result
    return sign * result