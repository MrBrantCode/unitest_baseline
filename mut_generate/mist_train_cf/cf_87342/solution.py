"""
QUESTION:
Write a function named `count_elements` that takes an array of integers as input, removes any duplicates, and returns a dictionary where the keys are the unique elements and the values are their counts in the original array. The function must have a time complexity of O(n) and a space complexity of O(n). It should not use any built-in methods or libraries for counting or removing duplicate elements.
"""

def count_elements(arr):
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return counts