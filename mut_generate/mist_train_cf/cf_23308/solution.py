"""
QUESTION:
Write a function `most_frequent_item(arr)` that takes an array of integers as input and returns the most frequent item in the array. If multiple items appear with the same highest frequency, return any one of them.
"""

def most_frequent_item(arr):
    """
    Finds the most frequent item in an array.
    """
    dictionary = {}
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    max_count = 0
    max_item = 0

    for k, v in dictionary.items():
        if v > max_count:
            max_item = k
            max_count = v
    return max_item