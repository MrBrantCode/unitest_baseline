"""
QUESTION:
Write a function called `compute_average` that takes a list of integers and two integers `range_start` and `range_end` as input. The function should calculate the average of the integers in the list that are within the range defined by `range_start` and `range_end` (inclusive). If no numbers are within the range, the function should return 0.
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