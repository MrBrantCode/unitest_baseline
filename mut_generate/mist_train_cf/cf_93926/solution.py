"""
QUESTION:
Design a function `is_palindrome(number)` that checks if a given non-negative integer is a palindrome. The function should have a time complexity of O(log n), where n is the number of digits in the input number, and use only constant space complexity without converting the number to a string or using any string manipulation functions.
"""

def is_palindrome(number):
    reverse = 0
    original = number

    while original > 0:
        last_digit = original % 10
        reverse = reverse * 10 + last_digit
        original = original // 10

    return number == reverse