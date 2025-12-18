"""
QUESTION:
Write a function `count_repeated_digits(phone_number)` that takes a string representing a phone number as input and returns the highest number of repeated digits in the phone number, where the phone number may contain non-digit characters and the repeated digits are only counted when they are the same digit.
"""

def count_repeated_digits(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))  
    digit_counts = [digits.count(digit) for digit in set(digits)]  
    return max(digit_counts) if digit_counts else 0 