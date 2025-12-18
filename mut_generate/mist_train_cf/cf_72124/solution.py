"""
QUESTION:
Write a function called `is_palindrome` that takes an integer as input and returns a boolean value indicating whether the integer is a palindrome. A palindrome is a number that remains the same when its digits are reversed. The function should work for non-negative integers.
"""

def is_palindrome(num):
    # convert the number to a string
    num_str = str(num)

    # reverse the string
    reversed_str = num_str[::-1]
    
    # compare the reversed string with the original string
    if num_str == reversed_str:
        return True
    else:
        return False