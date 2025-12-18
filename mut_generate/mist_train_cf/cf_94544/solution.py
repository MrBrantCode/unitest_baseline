"""
QUESTION:
Implement the `count_elements` function to take an array of integers as an argument and return a dictionary where keys are the unique elements from the array and values are their respective counts. The function should achieve this in O(n) time complexity and O(n) space complexity.
"""

def count_elements(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts