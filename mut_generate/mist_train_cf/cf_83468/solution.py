"""
QUESTION:
Write a function `search(array, target)` that finds and returns the indices of all occurrences of the `target` element in the given unsorted `array`. The function should return a list of indices, or an empty list if the `target` element is not found in the `array`.
"""

def search(array, target):
    result = []
    for i in range(len(array)):
        if array[i] == target:
            result.append(i)
    return result