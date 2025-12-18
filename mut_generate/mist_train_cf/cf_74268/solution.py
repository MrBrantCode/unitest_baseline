"""
QUESTION:
Create a function `is_perfect_square_palindrome` that checks if a given array of integers represents a palindromic sequence where each number in the sequence is a perfect square. The function should return True if the array is a perfect square palindrome and False otherwise. The array only contains integers.
"""

import math

def is_perfect_square_palindrome(arr):
    def is_perfect_square(n):
        root = int(math.sqrt(n))
        return n == root * root

    return arr == arr[::-1] and all(is_perfect_square(i) for i in arr)