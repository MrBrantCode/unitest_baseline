"""
QUESTION:
Write a function `max_palindrome` that takes a list of integers as input and returns the maximum integer that is a palindrome. A palindrome is a number that remains the same when its digits are reversed.
"""

def max_palindrome(num_list):
    """
    Returns the maximum integer that is a palindrome from a given list.

    Args:
        num_list (list): A list of integers.

    Returns:
        int: The maximum palindromic integer.
    """
    # Helper function to check if a number is palindrome
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    # Get only the palindrome numbers from the list
    palindromes = [n for n in num_list if is_palindrome(n)]

    # Get the max palindrome number from the list
    return max(palindromes) if palindromes else None