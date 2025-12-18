"""
QUESTION:
Write a function named `analyze_array` that takes a list of integers as input and returns a string or a dictionary based on the order of the array. The function should handle the following cases: 

- If the array is empty, return "The array is empty."
- If all elements in the array are the same, return "All elements are the same."
- If the array is in increasing order, return a string stating that the array is in increasing order and the percentage increase from the first to the last element.
- If the array is in decreasing order, return a string stating that the array is in decreasing order and the percentage decrease from the first to the last element.
- If the array is unordered, return a dictionary where the keys are the unique numbers in the array and the values are their corresponding counts.
"""

from collections import Counter

def analyze_array(arr):
    if len(arr) == 0:
        return "The array is empty."
    if len(set(arr)) == 1:
        return "All elements are the same."

    if arr == sorted(arr):
        return "The array is in increasing order by {}%.".format(((arr[-1] - arr[0]) / arr[0])*100)
    elif arr == sorted(arr, reverse=True):
        return "The array is in decreasing order by {}%.".format(((arr[0] - arr[-1]) / arr[0])*100)
    else:
        return dict(Counter(arr))