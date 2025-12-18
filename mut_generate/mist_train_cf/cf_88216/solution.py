"""
QUESTION:
Implement a function named `sum_and_count_digits` that takes a positive integer `n` as input, calculates the sum of its digits, and returns the sum along with the count of unique digits present in the number. The function should have a time complexity of O(n), where n is the number of digits in the integer, and a space complexity of O(1). The input integer can be very large (up to 10^18), and you cannot convert it to a string or use any built-in library functions for large number calculations.
"""

def sum_and_count_digits(n):
    # Calculate the sum of digits
    digit_sum = 0
    temp_n = n
    while temp_n > 0:
        digit_sum += temp_n % 10
        temp_n //= 10

    # Count the number of unique digits
    unique_digits = [0] * 10
    while n > 0:
        unique_digits[n % 10] = 1
        n //= 10
    digit_count = sum(unique_digits)

    return digit_sum, digit_count