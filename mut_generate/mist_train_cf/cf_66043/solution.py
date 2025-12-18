"""
QUESTION:
Implement a function `is_geometric_seq` that checks whether a given array of integers forms a geometric sequence. The function should return `True` if the series forms a geometric progression and `False` otherwise. Consider edge cases where the series contains zeros or negative numbers.
"""

def is_geometric_seq(arr):
    if len(arr) <= 1:
        return True

    if arr[1] == 0:
        for number in arr[2:]:
            if number != 0:
                return False
        return True

    ratio = arr[0] / arr[1]
    
    for i in range(len(arr) - 1):
        if arr[i+1] == 0 or (arr[i] / arr[i+1]) != ratio:
            return False

    return True