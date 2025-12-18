"""
QUESTION:
Implement a function named `sum_and_count_digits` that takes a large positive integer `n` (up to 10^18) as input and returns a tuple containing two values: the sum of its digits and the count of unique digits present in the number. The function should have a time complexity of O(n), where n is the number of digits in the integer, and a space complexity of O(1). Do not convert the integer to a string or use any built-in library functions for large number calculations.
"""

def sum_and_count_digits(n):
    digit_sum = 0
    unique_digits = [0] * 10
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        digit_sum += digit
        unique_digits[digit] = 1
        temp_n //= 10

    digit_count = sum(unique_digits)
    return digit_sum, digit_count