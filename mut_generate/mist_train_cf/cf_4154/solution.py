"""
QUESTION:
Implement a function `count_occurrences` that recursively counts the occurrences of a specific string `target` in the sub-arrays of a jagged array `arr` that have a length greater than a given threshold `lengthThreshold`. The function should have two base cases: one for an empty array and one for a sub-array with a length less than or equal to `lengthThreshold`. The function should only count occurrences in sub-arrays that meet the length condition and return the total count.
"""

def count_occurrences(arr, target, lengthThreshold):
    count = 0  

    if len(arr) == 0:
        return 0

    if len(arr[0]) <= lengthThreshold:
        return count_occurrences(arr[1:], target, lengthThreshold)

    for element in arr[0]:
        if element == target:
            count += 1

    count += count_occurrences(arr[1:], target, lengthThreshold)

    return count