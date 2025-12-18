"""
QUESTION:
Write a function named `most_frequent_item` that takes a list of integers as input and returns the most frequent item in the list. If there are multiple items with the same highest frequency, return the item that appears first in the list. Do not use any built-in Python functions for counting occurrences or finding the most frequent item.
"""

def most_frequent_item(num_list):
    counts = {}
    max_count = 0
    most_frequent = None

    for num in num_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > max_count:
            max_count = counts[num]
            most_frequent = num

    return most_frequent