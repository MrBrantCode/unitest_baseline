"""
QUESTION:
Given two integer arrays `arr1` and `arr2`, and an integer `d`, write a function `findTheDistanceValue(arr1, arr2, d)` that returns a tuple containing the count of elements in `arr1` such that there is no element in `arr2` within a distance `d`, and the indices of these elements in `arr1`. 

The distance between two elements is defined as the absolute difference between them. The function should only consider elements within the range `-10^3` to `10^3` and `0` to `100` for `d`. The length of both arrays should be between `1` and `500`.
"""

def findTheDistanceValue(arr1, arr2, d):
    indices = []
    count = 0
    for i, val1 in enumerate(arr1):
        for val2 in arr2:
            if abs(val1 - val2) <= d:
                break
        else:
            count += 1
            indices.append(i)
    return count, indices