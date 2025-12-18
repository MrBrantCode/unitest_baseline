"""
QUESTION:
Write a function named `compute_median` that calculates the median of a given list of numbers. The median is the middle value of the sorted list. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. The function should return the median as a floating-point number with two decimal places.
"""

def compute_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2-1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return round(median, 2)