"""
QUESTION:
Create a function `filter_and_sort(arr, num)` that takes a list of integers `arr` and an integer `num` as parameters. The function should return a new list containing elements from `arr` that are greater than `num`, with no duplicates, and sorted in descending order.
"""

def filter_and_sort(arr, num):
    return sorted(set([i for i in arr if i > num]), reverse=True)