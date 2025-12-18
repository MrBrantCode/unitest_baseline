"""
QUESTION:
Write a function `hasPairWithSum(nums, sum)` that takes an array of distinct integers `nums` and a target sum `sum` as input, and returns `True` if there exists a pair of integers in the array that adds up to the target sum, and `False` otherwise. The function should have a time complexity of O(N) and use O(N) auxiliary space, where N is the length of the input array.
"""

def hasPairWithSum(nums, sum):
    hashSet = set()
    for num in nums:
        diff = sum - num
        if diff in hashSet:
            return True
        hashSet.add(num)
    return False