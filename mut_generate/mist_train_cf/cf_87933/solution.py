"""
QUESTION:
Write a function `compute_average` that takes a list of integers and two integers `range_start` and `range_end` as input, and returns the average of the integers within the inclusive range from `range_start` to `range_end`. If no integers fall within the range, return 0.
"""

def compute_average(numbers, range_start, range_end):
    total = 0
    count = 0

    for num in numbers:
        if range_start <= num <= range_end:
            total += num
            count += 1

    if count == 0:
        return 0
    else:
        return total / count