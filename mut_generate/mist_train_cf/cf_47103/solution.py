"""
QUESTION:
Construct a function `handle_array(arr)` that replicates the input array `arr`, subtracts 7 from each numeric element, and handles non-numeric elements, null, and undefined values. The function should be computationally efficient to manage large arrays.
"""

def handle_array(arr):
    if not arr or len(arr) == 0:
        return []

    res = []
    for elem in arr:
        if isinstance(elem, (int, float)):
            res.append(elem - 7)
        else:
            res.append(elem)

    return res