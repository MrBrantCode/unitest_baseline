"""
QUESTION:
Write a function `count_repeated_digits(phone_number)` that takes a string phone number as input, which may contain special characters such as parentheses, hyphens, or spaces, and returns the highest count of repeated digits in the phone number.
"""

def count_repeated_digits(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))  # Extract digits from phone number
    digit_counts = [digits.count(digit) for digit in set(digits)]  # Count the occurrences of each digit
    return max(digit_counts) if digit_counts else 0  # Return the maximum count if there are any digits, else 0