"""
QUESTION:
Given an integer array `nums`, return the length of the longest wiggle subsequence of `nums` along with the subsequence itself. A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. A sequence with two or fewer elements is trivially a wiggle sequence. A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order. The input array `nums` will have a length between 1 and 1000, and each element will be an integer between 0 and 1000. The solution should have a time complexity of `O(n)`.
"""

def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums), nums

    prevdiff = nums[1] - nums[0]
    if prevdiff != 0:
        count = 2
        result = [nums[0], nums[1]]
    else:
        count = 1
        result = [nums[0]]

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i-1]
        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            count += 1
            result.append(nums[i])
            prevdiff = diff
    return count, result