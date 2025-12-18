"""
QUESTION:
Write a function named `find_duplicates` that takes a list of integers as input. The function should return a list of integers that appear more than three times in the input list, sorted in descending order.
"""

from collections import Counter

def find_duplicates(arr):
    # Count the occurrences of each element in the array
    counter = Counter(arr)
    
    # Filter the elements that appear more than three times and sort them in descending order
    return sorted([element for element, count in counter.items() if count > 3], reverse=True)