"""
QUESTION:
Calculate the average, median, and mode of a list of numbers.

Create a function named `calculate_stats` that takes a list of numbers as input. The function should return the average, median, and mode(s) of the input list. If there are multiple modes, return them as a list.
"""

from collections import Counter
import statistics

def calculate_stats(numbers):
    # First, we calculate the mean (average) using the mean function from the statistics library
    average = statistics.mean(numbers)

    # Then, we calculate the median, also using a function from the statistics library
    median = statistics.median(numbers)

    # For the mode, we first use a Counter to count how many times each number appears in the list
    freqs = Counter(numbers)
    
    # We then find the highest frequency
    highest_freq = max(freqs.values())
    
    # And we get all numbers that have this highest frequency
    modes = [num for num, freq in freqs.items() if freq == highest_freq]

    return average, median, modes