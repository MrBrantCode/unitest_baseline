"""
QUESTION:
Write a function `find_second_most_frequent` that takes an array of integers as input, returns the second most frequent element that appears more than once. If no such element exists, the function may return any value or handle the case as desired.
"""

from collections import Counter

def find_second_most_frequent(arr):
    # Count the frequency of each element in the array
    counter = Counter(arr)
    
    # Get a list of elements with their frequencies in descending order
    frequencies = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # Find the second most frequent element that is not a duplicate
    for element, count in frequencies[1:]:
        if count > 1:
            return element