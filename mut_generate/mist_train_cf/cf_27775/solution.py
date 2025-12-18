"""
QUESTION:
Write a function `calculateDigitSum` that takes a non-negative integer `number` as input and returns the sum of its digits. For example, `calculateDigitSum(123)` should return `6` (1 + 2 + 3 = 6).
"""

def calculateDigitSum(number):
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number = number // 10
    return digit_sum