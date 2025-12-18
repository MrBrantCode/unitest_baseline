"""
QUESTION:
Write a function called `find_unique_elements` that takes an array of integers as input and returns a list of elements that appear exactly once in the array. The function should have a time complexity of O(n) and return the elements in the order of their first occurrence. It should handle negative numbers and zero as valid elements, exclude duplicates, and return an empty list if there are no unique elements.
"""

def find_unique_elements(arr):
    counts = {}
    unique_elements = []

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count == 1:
            unique_elements.append(num)

    return unique_elements