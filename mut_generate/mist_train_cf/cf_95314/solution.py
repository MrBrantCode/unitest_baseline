"""
QUESTION:
Write a function `sum_of_digits_and_count_unique_digits` that takes a positive integer `n` as input, calculates the sum of its digits, and returns a tuple containing the sum of digits and the count of unique digits present in the number. The function should have a time complexity of O(n), where n is the number of digits in the integer, and a space complexity of O(1).
"""

def sum_of_digits_and_count_unique_digits(n):
    # Initialize variables
    digit_sum = 0
    unique_digits = set()

    # Iterate over each digit in the number
    while n > 0:
        digit = n % 10  # Extract the rightmost digit
        digit_sum += digit  # Add the digit to the sum
        unique_digits.add(digit)  # Add the digit to the set of unique digits
        n //= 10  # Remove the rightmost digit from the number

    # Return the sum of digits and the count of unique digits
    return digit_sum, len(unique_digits)