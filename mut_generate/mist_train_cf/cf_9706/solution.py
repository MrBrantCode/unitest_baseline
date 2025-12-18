"""
QUESTION:
Create a function `create_palindrome` that takes a string of lowercase alphabets as input and returns the palindrome created by appending the reverse of the input string to the original string. The function should have a time complexity of O(n^2) and should not use any additional data structures.
"""

def create_palindrome(s):
    """
    This function creates a palindrome from a given string of lowercase alphabets.
    
    Parameters:
    s (str): The input string of lowercase alphabets.
    
    Returns:
    str: The palindrome created by appending the reverse of the input string to the original string.
    """
    palindrome = ""
    for c in s[::-1]:
        palindrome += c
    palindrome += s
    return palindrome