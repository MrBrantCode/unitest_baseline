"""
QUESTION:
Write a function called `aggregate_even_sum` that takes two parameters, `start` and `end`, representing a range of consecutive integers. The function should calculate and return the sum of all even integers within this range, excluding the `end` value. Ensure the function works for any valid integer range.
"""

def aggregate_even_sum(start, end):
    sum = 0
    for num in range(start, end):
        if num % 2 == 0:   # checks if the number is even
            sum += num
    return sum