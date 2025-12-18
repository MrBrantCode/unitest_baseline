"""
QUESTION:
Write a function `median_in_interval` that takes a list of integers `l` and two integers `lower_limit` and `upper_limit` as input. The function should return `True` if the median of the integers in the list `l` falls within the interval defined by `lower_limit` and `upper_limit` (inclusive), and `False` otherwise. Note that the list `l` may contain an even or odd number of elements.
"""

def median_in_interval(numbers, lower_limit, upper_limit):
    numbers.sort()
    if len(numbers) % 2 == 0:  # Even number of elements
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:  # Odd number of elements
        median = numbers[len(numbers)//2]
    return lower_limit <= median <= upper_limit