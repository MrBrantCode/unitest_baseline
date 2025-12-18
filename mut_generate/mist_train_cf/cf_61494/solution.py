"""
QUESTION:
Write a function called `merge_without_duplicates` that takes two arrays `array1` and `array2` as input and returns a new array containing all unique elements from both arrays, without using built-in functions for merging and removing duplicates.
"""

def merge_without_duplicates(array1, array2):
    result = []

    for item in array1:
        if item not in result:
            result.append(item)
            
    for item in array2:
        if item not in result:
            result.append(item)

    return result