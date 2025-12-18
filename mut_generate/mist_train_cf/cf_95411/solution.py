"""
QUESTION:
Write a function named `find_most_frequent` that takes a list of integers as input and returns the most frequent item in the list. If there are multiple items with the same highest frequency, return the item that appears first in the list. The solution should not use built-in Python functions for counting occurrences or finding the most frequent item and have a time complexity of O(n), where n is the length of the input list.
"""

def find_most_frequent(lst):
    frequency = {}
    most_frequent_item = None
    max_frequency = 0

    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

        if frequency[item] > max_frequency:
            max_frequency = frequency[item]
            most_frequent_item = item

    return most_frequent_item