"""
QUESTION:
Write a function `calculate_mode` that takes a list of floating point numbers as input and returns the mode, which is the value that appears most frequently. The function should use the `Counter` class from the `collections` module to count the occurrences of each number. The function should return the most common number.
"""

from collections import Counter

def calculate_mode(nums):
    # Calculate the frequency of each number
    num_freq = Counter(nums)

    # Find the occurrences  
    modes = num_freq.most_common()

    # Take the most common one
    mode = modes[0][0]
    return mode