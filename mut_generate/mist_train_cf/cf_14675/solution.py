"""
QUESTION:
Write a function `is_palindrome(n)` that checks if the given number `n` is a palindrome. The function should have a time complexity of O(log n), where n is the number of digits in the input number, and use a constant amount of additional space.
"""

def entance(n):
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