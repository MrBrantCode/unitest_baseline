"""
QUESTION:
Create a function `is_palindrome(n)` that takes a numerical sequence `n` as input and returns a boolean value indicating whether the sequence constitutes a palindromic number. The function should be able to handle any numerical sequence, without any restrictions on its size or content.
"""

def is_palindrome(n):
    # Convert the number into string
    num_str = str(n)
    # Compare the string with its reverse
    return num_str == num_str[::-1]