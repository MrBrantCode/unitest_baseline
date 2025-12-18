"""
QUESTION:
Write a function called `is_palindrome` that takes a non-negative integer as input and returns True if the number is a palindrome and False otherwise. The function should have a time complexity of O(log n) where n is the number of digits in the input number and a space complexity of O(1). The function should not convert the input number to a string or use any string manipulation functions.
"""

def entance(number):
    reverse = 0
    original = number

    while original > 0:
        last_digit = original % 10
        reverse = reverse * 10 + last_digit
        original = original // 10

    return number == reverse