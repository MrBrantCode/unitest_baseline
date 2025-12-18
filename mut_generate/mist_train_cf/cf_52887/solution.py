"""
QUESTION:
Design a function `findTarget` that takes a 2D array `nums` and a target integer `target` as input. The 2D array consists of distinct integers sorted in ascending order in each row, but the number of elements in each row can vary. The function should return the position of the target integer in the form of (row, column) if found, and (-1, -1) otherwise. The time complexity of the function should be less than O(n^2).
"""

def findTarget(nums, target):
    row, col = len(nums), len(nums[0])
    lo, hi = 0, row*col
    while lo < hi:
        mid = (lo + hi) // 2
        x = nums[mid // col][mid % col]
        if x < target:
            lo = mid + 1
        elif x > target:
            hi = mid 
        else:
            return (mid // col, mid % col) # Return position in row,column format
    return (-1, -1) # Return -1,-1 if target is not present in array