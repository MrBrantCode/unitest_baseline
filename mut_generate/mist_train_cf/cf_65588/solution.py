"""
QUESTION:
Write a function named `intersect` that takes two lists of integers as input and returns a list of the intersecting elements between the two input lists. The function should return the intersecting elements in any order and without duplicates.
"""

def intersect(arr1, arr2):
    # Converts both lists to sets and use the intersection() method to get the intersecting values.
    return list(set(arr1) & set(arr2))