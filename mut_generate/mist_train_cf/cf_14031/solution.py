"""
QUESTION:
Write a function `reverse_and_sum` that takes an integer `num` as input and returns the reversed integer and the sum of its digits. The function should operate under the following constraints: time complexity O(logN) and space complexity O(1).
"""

def reverse_and_sum(num):
    reverse = 0
    digit_sum = 0

    while num != 0:
        last_digit = num % 10
        digit_sum += last_digit
        reverse = reverse * 10 + last_digit
        num //= 10

    return reverse, digit_sum