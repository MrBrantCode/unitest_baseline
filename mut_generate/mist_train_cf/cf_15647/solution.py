"""
QUESTION:
Write a function named `find_second_most_frequent` that takes an array of integers as input and returns the second most frequent non-unique element in the array. The function should ignore unique elements and consider only elements that appear more than once. If there are multiple elements with the same second highest frequency, any of them can be returned. The function should return the element itself, not its frequency.
"""

from collections import Counter

def find_second_most_frequent(arr):
    # Count the frequency of each element in the array
    counter = Counter(arr)
    
    # Get a list of elements with their frequencies in descending order
    frequencies = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # Find the second most frequent element that is not a duplicate
    for element, count in frequencies:
        if count > 1:
            return element