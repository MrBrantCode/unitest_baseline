"""
QUESTION:
Calculate the sum of all digits in a sequence that match the next digit. The sequence is circular, meaning the last digit is compared to the first. Write a function `calculate_matching_sum` that takes a string of digits as input and returns the sum of matching digits. The input string only contains digits and has a length of at least 1. The function should return 0 if no digits match.
"""

def calculate_matching_sum(captcha: str) -> int:
    captcha = captcha + captcha[0]  # Append the first digit to the end to consider circular matching
    matching_sum = sum(int(captcha[i]) for i in range(1, len(captcha)) if captcha[i] == captcha[i - 1])
    return matching_sum