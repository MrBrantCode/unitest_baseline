"""
QUESTION:
Write a function `find_most_frequent_element(lst)` that finds the element that occurs most frequently in a list `lst` containing at least 10 elements, including possible negative numbers. The function should return the most frequent element.
"""

from collections import Counter

def find_most_frequent_element(lst):
    # Create a counter object from the list
    counter = Counter(lst)
    
    # Find the most common element and its frequency
    most_common = counter.most_common(1)
    
    # Return the most common element
    return most_common[0][0]