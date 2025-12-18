"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median of the list. The function should handle both even and odd-length lists. If the input list is empty, it should return 0.
"""

def median(data):
    data.sort()
    length = len(data)
    if length == 0:
        return 0
    if length % 2 == 0:
        return (data[length // 2] + data[length // 2 - 1]) / 2
    elif length % 2 == 1:
        return data[length // 2]