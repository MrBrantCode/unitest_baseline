"""
QUESTION:
Write a function named `is_palindrome` that takes an integer `n` as input and returns a boolean indicating whether the integer is a palindrome or not. The function should have a time complexity of O(log n), where n is the number of digits in the input number, and use a constant amount of additional space. The function should consider that a negative number cannot be a palindrome.
"""

def is_palindrome(n):
    if n < 0:
        return False

    divisor = 1
    while n // divisor >= 10:
        divisor *= 10

    while n != 0:
        left = n // divisor
        right = n % 10

        if left != right:
            return False

        n = (n % divisor) // 10
        divisor //= 100

    return True