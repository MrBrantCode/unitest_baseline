"""
QUESTION:
Write a function named `calculate_median` that takes an unsorted list of numbers as input and returns the median value of the list. The function should sort the list if necessary, then calculate the median without using any built-in sorting or median calculation functions. The list may contain an even or odd number of elements.
"""

def calculate_median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n//2]
    else:
        return (data[n//2 - 1] + data[n//2]) / 2