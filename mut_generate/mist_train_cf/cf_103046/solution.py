"""
QUESTION:
Write a function `calculate_mean_median_mode` that calculates the mean, median, and mode of a given array of integers. The array will always have at least one element and can contain both positive and negative integers. The function should return or print the mean, median, and mode. If there are multiple modes, any one of them can be returned.
"""

from collections import Counter
import statistics

def calculate_mean_median_mode(numbers):
    mean = sum(numbers) / len(numbers)
    
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[len(sorted_numbers)//2 - 1] + sorted_numbers[len(sorted_numbers)//2]) / 2
    else:
        median = sorted_numbers[len(sorted_numbers)//2]
    
    counts = Counter(numbers)
    max_count = max(counts.values())
    mode = next(number for number, count in counts.items() if count == max_count)
    
    return mean, median, mode