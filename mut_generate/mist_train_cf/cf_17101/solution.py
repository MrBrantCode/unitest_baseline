"""
QUESTION:
Write a function named `count_elements` that takes an array of integers as an argument and returns a dictionary where the keys are the unique elements from the array and the values are their respective counts. The function should achieve this with a time complexity of O(n) and a space complexity of O(n).
"""

def count_elements(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts