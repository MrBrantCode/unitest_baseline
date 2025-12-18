"""
QUESTION:
Write a function named `find_highest_frequency_number` that takes a list of integers as input and returns the number greater than 100 that appears with the highest frequency. If there are multiple numbers with the same highest frequency, the function should return one of them.
"""

from collections import Counter

def find_highest_frequency_number(numbers):
    """
    This function takes a list of integers as input and returns the number greater than 100 
    that appears with the highest frequency. If there are multiple numbers with the same 
    highest frequency, the function returns one of them.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The number greater than 100 with the highest frequency.
    """
    # create a Counter object to count frequency of each number
    counter = Counter(numbers)
    
    # filter out numbers that are more than 100
    filtered_numbers = {k: v for k, v in counter.items() if k > 100}
    
    # find the number with maximum frequency
    max_freq_num = max(filtered_numbers, key=filtered_numbers.get)
    
    return max_freq_num