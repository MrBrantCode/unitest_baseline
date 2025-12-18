"""
QUESTION:
Create a function `containsNearbyDuplicate(nums, k)` that takes an array of integers `nums` and an integer `k` as input. The function should return `True` if there exist two identical elements in the array with an absolute index difference not exceeding `k`, and `False` otherwise.
"""

def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False