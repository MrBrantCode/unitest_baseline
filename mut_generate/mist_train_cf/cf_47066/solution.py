"""
QUESTION:
Create a function named `unique_elements` that takes two arrays of string values as input and returns the total number of elements that are unique to one of the arrays, not common to both. The function should not return the unique elements themselves, just their count.
"""

def unique_elements(arr1, arr2):
    combined = arr1 + arr2
    occurrences = {}
    for el in combined:
        if el in occurrences:
            occurrences[el] += 1
        else:
            occurrences[el] = 1
    unique_count = sum(1 for el, count in occurrences.items() if count == 1)
    return unique_count