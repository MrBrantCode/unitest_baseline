"""
QUESTION:
Given a function named `numIdenticalPairs` that takes two parameters, `nums` (an array of integers) and `k` (an integer). A pair `(i,j)` is considered good if `nums[i]` equals `nums[j]`, `i` is less than `j`, and `j-i` is less than or equal to `k`. Return the number of good pairs. The function must work under the constraints that the length of `nums` is between 1 and 100 inclusive, each element in `nums` is between 1 and 100 inclusive, and `k` is between 1 and the length of `nums` inclusive.
"""

def numIdenticalPairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and j-i <= k:
                count += 1
    return count