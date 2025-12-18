"""
QUESTION:
Create a function 'checkInteger' that takes a number and returns four boolean values: 
1. True if the number is an integer, False otherwise.
2. True if the number is a perfect square, False otherwise.
3. True if the number is a prime number, False otherwise.
4. True if the absolute value of the number is a palindrome, False otherwise.

The function should handle numbers within the range of -10^18 to 10^18, and handle non-numeric inputs, NaN, infinity, and negative infinity correctly.
"""

import math

def checkInteger(num):
    """
    Checks if a given number is an integer, perfect square, prime number, and palindrome.

    Args:
        num: The input number.

    Returns:
        A tuple of four boolean values indicating whether the number is an integer, 
        perfect square, prime number, and palindrome respectively.
    """
    is_int = isinstance(num, int) and not math.isnan(num) and num != float('inf') and num != float('-inf')
    is_perfect_square = is_int and num >= 0 and math.isqrt(num) ** 2 == num
    is_prime = is_int and num > 1 and all(num % i != 0 for i in range(2, math.isqrt(num) + 1))
    is_palindrome = is_int and str(abs(num)) == str(abs(num))[::-1]
    return is_int, is_perfect_square, is_prime, is_palindrome