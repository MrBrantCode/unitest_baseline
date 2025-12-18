"""
QUESTION:
Create a function named `reverse_and_sum` that takes an integer as input and returns the sum of the digits of its reverse. The function should handle both positive and negative integers, preserving the sign in the reversed integer. If the reversed integer overflows, return 0. The function must run in O(logN) time complexity and use O(1) space complexity.
"""

def reverse_and_sum(num: int) -> int:
    """
    This function takes an integer as input, reverses it, and returns the sum of its digits.
    It handles both positive and negative integers, preserving the sign in the reversed integer.
    If the reversed integer overflows, it returns 0.
    
    The time complexity is O(logN) and the space complexity is O(1).

    Args:
        num (int): The input integer.

    Returns:
        int: The sum of the digits of the reversed integer.
    """
    
    # Initialize variables
    reverse = 0
    total_sum = 0
    is_negative = False
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    
    # Check if the number is negative
    if num < 0:
        is_negative = True
        num = -num
    
    # Reverse the number and calculate the sum of its digits
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        total_sum += last_digit
        num //= 10
    
    # Preserve the sign
    if is_negative:
        reverse = -reverse
    
    # Check for overflow
    if reverse > INT_MAX or reverse < INT_MIN:
        return 0
    
    return total_sum