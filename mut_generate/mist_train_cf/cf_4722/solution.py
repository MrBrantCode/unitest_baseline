"""
QUESTION:
Write a function named `count_digit_in_range` that takes three parameters: `start`, `end`, and `digit`. This function should return the total number of occurrences of the given `digit` in all numbers within the range `start` to `end` (inclusive) that are divisible by 7. The `digit` can be part of a larger number.
"""

def count_digit_in_range(start, end, digit):
    count = 0
    for num in range(start, end + 1):
        if num % 7 == 0:
            count += str(num).count(str(digit))
    return count