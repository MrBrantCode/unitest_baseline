"""
QUESTION:
Write a function `sort_elements` that takes a list of integers as input and returns a new list where the elements are sorted based on their frequency in descending order. If multiple elements have the same frequency, they should be sorted in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
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