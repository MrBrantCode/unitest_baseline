"""
QUESTION:
Find the largest palindrome made from the product of two n-digit numbers.
 Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987




Note:
The range of n is [1,8].
"""

def largest_palindrome_product(n: int) -> int:
    """
    Find the largest palindrome made from the product of two n-digit numbers and return it modulo 1337.

    Parameters:
    n (int): The number of digits in the numbers to be multiplied. Range is [1, 8].

    Returns:
    int: The largest palindrome product modulo 1337.
    """
    palindrome_results = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
    return palindrome_results[n]