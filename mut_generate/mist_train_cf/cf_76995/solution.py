"""
QUESTION:
Write a function `identify_number` that takes an array of integers as input and returns the number greater than 100 that appears most frequently in the array.
"""

from collections import Counter

def identify_number(arr):
    # Filter out numbers that are over 100
    over_100 = [num for num in arr if num > 100]

    # Find the most common number
    counter = Counter(over_100)
    most_common = counter.most_common(1)[0]

    return most_common[0]