"""
QUESTION:
Write a function named `get_median_and_sorted_array` that takes two lists of integers, `arr1` and `arr2`, as input. The function should combine the elements of both lists and sort them in ascending order without using any built-in or third-party sorting methods. The function should also calculate the median of the new array. If the array has an even number of items, the median should be the average of the two middle items. Return the sorted array and the median.
"""

def entrance(arr1, arr2):
    merged = arr1 + arr2
    for i in range(len(merged)):
        for j in range(len(merged) - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    length = len(merged)
    if length % 2 == 0:
        median = (merged[length // 2] + merged[length // 2 - 1]) / 2
    else:
        median = merged[length // 2]

    return merged, median