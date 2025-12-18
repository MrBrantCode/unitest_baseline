"""
QUESTION:
Write a function named `custom_sort` that takes a list of dictionaries as input and returns the sorted list. The function should sort the list based on the "priority" key, with tasks having a priority of 1 at the beginning and tasks having a priority of 10 at the end. For tasks with a priority between 2 and 9 (inclusive), they should be sorted in ascending order based on their "name" key. If two tasks have the same priority and name, the one with the lower "id" key should come first in the sorted list. The function should not take any other parameters besides the input list.
"""

def custom_sort(data):
    return sorted(data, key=lambda x: (x["priority"], x["name"] if 1 < x["priority"] < 10 else '', x["id"]))