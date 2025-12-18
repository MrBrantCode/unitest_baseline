"""
QUESTION:
Implement the `calculate_descriptive_statistics` function to calculate the mean, median, mode, range, variance, and standard deviation of a given list of numerical values. The function should accept a list of numbers and return a dictionary containing the calculated descriptive statistics. The input list will always contain at least one numerical value.
"""

from statistics import mean, median, variance, stdev
from collections import Counter

def calculate_descriptive_statistics(data: list) -> dict:
    descriptive_stats = {}
    
    descriptive_stats['mean'] = mean(data)
    descriptive_stats['median'] = median(data)
    
    data_counter = Counter(data)
    max_count = max(data_counter.values())
    modes = [num for num, count in data_counter.items() if count == max_count]
    descriptive_stats['mode'] = modes if len(modes) > 1 else modes[0]
    
    descriptive_stats['range'] = max(data) - min(data)
    descriptive_stats['variance'] = variance(data)
    descriptive_stats['standard_deviation'] = stdev(data)
    
    return descriptive_stats