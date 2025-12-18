"""
QUESTION:
Write a function called `is_palindrome` that takes an integer as input and returns a boolean indicating whether the absolute value of the integer is a palindrome when considering only alphanumeric characters and ignoring case. The function should work for integers of any size.
"""

def is_palindrome(num):
    str_num = str(abs(num))  
    alphanumeric_str = ''.join(e for e in str_num if e.isalnum())  
    lower_str = alphanumeric_str.lower()  
    reverse_str = lower_str[::-1]  
    return lower_str == reverse_str  