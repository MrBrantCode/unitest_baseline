"""
QUESTION:
Create a function `filter_palindrome_prime_tuples` that takes a list of tuples as input, where each tuple contains a string and an integer. Return a new list containing only the tuples where the string is a palindrome and the integer is a prime number. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(k), where k is the number of tuples that satisfy the conditions.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def filter_palindrome_prime_tuples(tuples_list):
    """
    Filter a list of tuples to include only those where the string is a palindrome 
    and the integer is a prime number.

    Args:
        tuples_list (list): A list of tuples containing a string and an integer.

    Returns:
        list: A list of tuples where the string is a palindrome and the integer is a prime number.
    """
    return [(s, n) for s, n in tuples_list if is_palindrome(s) and is_prime(n)]