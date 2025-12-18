"""
QUESTION:
Create a recursive function `digit_frequency` that takes an integer `n` as input and returns a tuple containing a dictionary of digit frequencies and the most and least frequent digits. The function should have a time complexity of O(n), where n is the number of digits in the input number. The dictionary should have digits as keys and their frequencies as values. If two digits have the same maximum or minimum frequency, the function should return the smallest digit.
"""

from collections import defaultdict

def digit_frequency(n):
    digit_counts = defaultdict(int)
    max_digit, min_digit = None, None
    max_count, min_count = -float('inf'), float('inf')

    def helper(n):
        nonlocal max_digit, min_digit, max_count, min_count
        if n == 0:
            return

        digit = n % 10
        digit_counts[digit] += 1

        if digit_counts[digit] > max_count or (digit_counts[digit] == max_count and digit < max_digit):
            max_digit = digit
            max_count = digit_counts[digit]

        if digit_counts[digit] < min_count or (digit_counts[digit] == min_count and digit < min_digit):
            min_digit = digit
            min_count = digit_counts[digit]

        helper(n // 10)

    helper(n)

    return digit_counts, max_digit, min_digit