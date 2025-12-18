"""
QUESTION:
Implement the function `search_in_rotated_array(alist, target)` that takes a rotated sorted array `alist` of distinct integers and a target value `target` as input, and returns the index of the target value in the array if found, or -1 if not found. The array does not contain duplicates and can be rotated in either direction.
"""

def search_in_rotated_array(alist, target):
    leftix, rightix = 0, len(alist) - 1

    while leftix <= rightix:
        midpoint = (leftix + rightix) // 2
        if alist[midpoint] == target:
            return midpoint

        if alist[leftix] <= alist[midpoint]:
            if alist[leftix] <= target < alist[midpoint]:
                rightix = midpoint - 1
            else:
                leftix = midpoint + 1
        else:
            if alist[midpoint] < target <= alist[rightix]:
                leftix = midpoint + 1
            else:
                rightix = midpoint - 1

    return -1