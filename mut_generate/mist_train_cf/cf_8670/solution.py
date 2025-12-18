"""
QUESTION:
Create a function 'checkInteger' that takes a number as input and returns a list of boolean values indicating whether the number is an integer, a perfect square, a prime number, and a palindrome.

The function should handle the following constraints and edge cases:
- The input number should be within the range of -10^18 to 10^18.
- The function should return false for any non-numeric input.
- The function should return false for NaN (Not a Number) values.
- The function should return false for infinity and negative infinity values.
- The function should handle extremely large numbers efficiently without causing memory or performance issues.
- The function should handle floating-point numbers correctly and consider them as non-integers.
- The function should handle decimal numbers correctly and consider them as non-integers.
- The function should handle numbers in scientific notation correctly and consider them as non-integers.
- The function should handle zero correctly and consider it as an integer and a perfect square, but not a prime number or a palindrome.
- The function should handle negative zero correctly and consider it as an integer, a perfect square, but not a prime number or a palindrome.
- The function should handle negative integers correctly and consider them as integers, but not as perfect squares, prime numbers, or palindromes.
- The function should handle non-integer negative numbers correctly and consider them as non-integers, non-perfect squares, non-prime numbers, and non-palindromes.
- The function should handle non-integer positive numbers correctly and consider them as non-integers, non-perfect squares, non-prime numbers, and non-palindromes.
"""

import math

def checkInteger(num):
    is_int = isinstance(num, int) and not math.isnan(num) and num != float('inf') and num != float('-inf')
    is_perfect_square = False
    if is_int and num >= 0:
        is_perfect_square = math.isqrt(num) ** 2 == num
    is_prime = False
    if is_int and num >= 2:
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                is_prime = False
                break
        else:
            is_prime = True
    is_palindrome = False
    if is_int:
        num_str = str(abs(num))
        is_palindrome = num_str == num_str[::-1]
    return [is_int, is_perfect_square, is_prime, is_palindrome]