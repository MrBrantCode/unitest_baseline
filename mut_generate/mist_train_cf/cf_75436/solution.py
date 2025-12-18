"""
QUESTION:
Create a function named 'is_palindrome' that determines whether a given numeric value is a palindrome. The function should return True if the numeric value remains the same when its digits are reversed, and False otherwise. The input is a numeric value.
"""

def is_palindrome(n):
    n = str(n)  # Convert the number to a string
    return n == n[::-1]  # Check if the string is the same when read backwards