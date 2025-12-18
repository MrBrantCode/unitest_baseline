"""
QUESTION:
Write a function `find_distance_value(arr1, arr2, d)` that takes two integer arrays `arr1` and `arr2`, and an integer `d` as input, and returns a tuple containing the count and list of elements in `arr1` that have an absolute difference greater than `d` with all elements in `arr2`.

Constraints: 
- `1 <= arr1.length, arr2.length <= 500`
- `-10^3 <= arr1[i], arr2[j] <= 10^3`
- `0 <= d <= 100`
"""

def find_distance_value(arr1, arr2, d):
    output = [i for i in arr1 if all(abs(i-j) > d for j in arr2)]
    return len(output), output