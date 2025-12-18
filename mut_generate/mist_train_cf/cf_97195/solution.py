"""
QUESTION:
Write a function `sort_elements` that takes a list of integers as input and returns a list of integers sorted in descending order of frequency. If multiple elements have the same frequency, they should be sorted in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_elements(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_elements = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))

    return sorted_elements