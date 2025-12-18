"""
QUESTION:
Write a function named `find_most_frequent_element` that finds the most frequently occurring element in a list of integers. The list must have a minimum length of 10 elements and may contain negative numbers. The function should return the most frequent element.
"""

from collections import Counter

def find_most_frequent_element(lst):
    # Create a counter object from the list
    counter = Counter(lst)
    
    # Find the most common element and its frequency
    most_common = counter.most_common(1)
    
    # Return the most common element
    return most_common[0][0]