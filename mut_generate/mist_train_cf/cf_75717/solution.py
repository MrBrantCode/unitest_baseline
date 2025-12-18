"""
QUESTION:
Create a function `cumulative_sum_even_numbers` that takes two integers, `start` and `end`, as parameters. The function should return the cumulative sum of even integers from `start` to `end` (inclusive).
"""

def cumulative_sum_even_numbers(start, end):
    even_sum = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_sum += i
    return even_sum