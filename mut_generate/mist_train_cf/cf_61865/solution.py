"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median value. The list can contain an unbalanced mixture of even and odd numbers, and the function should not use any list sorting methods. Note that this constraint means the function will not always return the exact median, but rather an approximation of it.
"""

def median(numbers):
    n = len(numbers)
    s = sum(numbers)
    avg = s/n

    least_diff = float("inf")
    median = 0

    for num in numbers:
        diff = abs(num-avg)
        if diff < least_diff:
            least_diff = diff
            median = num
            
    return median