"""
QUESTION:
Create a function `count_digit_occurrences(start, end, digit)` that takes three parameters: `start` (the starting number of the range, inclusive), `end` (the ending number of the range, inclusive), and `digit` (the specific digit to count occurrences of). The function should return the total number of occurrences of the `digit` in the numbers within the given range.
"""

def count_digit_occurrences(start, end, digit):
    count = 0
    for num in range(start, end + 1):
        count += str(num).count(str(digit))
    return count