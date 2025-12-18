"""
QUESTION:
Write a function `normalize_and_sort` that takes a list of numbers as input, sorts the list in ascending order, removes any negative values, calculates the sum of the remaining values, normalizes each value by dividing it by the sum, and returns the normalized values sorted in descending order. The input list can contain both positive and negative integers.
"""

def normalize_and_sort(data):
    data.sort()
    data = [x for x in data if x >= 0]
    total = sum(data)
    normalized = [x / total for x in data]
    normalized.sort(reverse=True)
    return normalized