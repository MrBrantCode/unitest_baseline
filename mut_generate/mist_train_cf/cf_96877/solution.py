"""
QUESTION:
Write a function `find_next_palindrome(N)` that finds the next smallest palindrome greater than the given integer N. A palindrome is a number that reads the same forward and backward. If N is already a palindrome, the function should return the next smallest palindrome greater than N.
"""

def find_next_palindrome(N):
    """
    Finds the next smallest palindrome greater than the given integer N.

    Args:
        N (int): The input integer.

    Returns:
        int: The next smallest palindrome greater than N.
    """
    def is_palindrome(num):
        num_str = str(num)
        if len(num_str) <= 1:
            return True
        if num_str[0] == num_str[-1]:
            return is_palindrome(num_str[1:-1])
        return False

    prime = N + 1
    while True:
        if is_palindrome(prime):
            return prime
        prime += 1