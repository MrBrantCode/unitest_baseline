"""
QUESTION:
You are given a function `canReachEnd(arr)` and an array `arr` of non-negative integers representing the maximum jump length at each position. The function should return `True` if it is possible to reach the last index from the first index, and `False` otherwise, with the assumption that you can always reach the last index.
"""

def canReachEnd(arr):
    def helper(pos, seen):
        if pos < 0 or pos >= len(arr) or pos in seen:
            return False
        if pos == len(arr) - 1:
            return True
        seen.add(pos)
        return helper(pos + arr[pos], seen) or helper(pos - arr[pos], seen)

    seen = set()
    return helper(0, seen)