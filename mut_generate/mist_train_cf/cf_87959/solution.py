"""
QUESTION:
Create a function named `is_palindrome` that determines if a given integer is a palindrome without converting it to a string. The function should be efficient for large numbers and consider negative numbers. The function should return a boolean value indicating whether the input number is a palindrome or not.
"""

def is_palindrome(number):
    if number < 0:
        return False
    elif number < 10:
        return True
    
    original_number = number
    reversed_number = 0
    
    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number // 10
    
    return original_number == reversed_number