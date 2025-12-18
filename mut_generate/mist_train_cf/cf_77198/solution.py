"""
QUESTION:
Create a Python function `is_palindrome` that determines whether a given character sequence is a palindrome using recursion. The function should not use any built-in functions for string reversal. The input is a string and the output is a boolean value indicating whether the string is a palindrome or not.
"""

def is_palindrome(input_string):
    # Base case: if the string is empty or has one character IT IS a palindrome.
    if len(input_string) < 2:
        return True
  
    # If the first and last characters are equal, we continue to check the next characters (excluding first and last)
    # We are reducing our problem's size in a recursive way
    if input_string[0] == input_string[-1]:
        return is_palindrome(input_string[1:-1])

    # If the first and the last character was not equal, IT IS NOT a palindrome
    return False