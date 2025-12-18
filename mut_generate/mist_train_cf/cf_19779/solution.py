"""
QUESTION:
Write a function `calculate_statistics` that takes a list of numbers and returns the mean, median, mode, and standard deviation of that list. The function should skip non-numeric values during calculations and return None for all measures if the list is empty or contains only non-numeric values. The mode should be returned as a list of the most frequent values.
"""

import math
from collections import Counter

def calculate_statistics(numbers):
    if len(numbers) == 0:
        return None, None, None, None
    
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if len(numeric_numbers) == 0:
        return None, None, None, None
    
    mean = sum(numeric_numbers) / len(numeric_numbers)
    
    sorted_numbers = sorted(numeric_numbers)
    mid_index = len(sorted_numbers) // 2
    median = sorted_numbers[mid_index] if len(sorted_numbers) % 2 != 0 else (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    
    count_dict = Counter(sorted_numbers)
    max_freq = max(count_dict.values())
    mode = [num for num, freq in count_dict.items() if freq == max_freq]
    
    variance = sum([(num - mean) ** 2 for num in numeric_numbers]) / len(numeric_numbers)
    standard_deviation = math.sqrt(variance)
    
    return mean, median, mode, standard_deviation