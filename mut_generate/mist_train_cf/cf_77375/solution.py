"""
QUESTION:
Write a function named `maximumUniqueSubarray` that takes an array of positive integers `nums` as input. The function should return the maximum possible score that can be obtained by erasing precisely one subarray with unique elements, where the score is the sum of the elements in the subarray. The input array `nums` has a length within the range of 1 <= nums.length <= 10^5 and its elements are within the range of 1 <= nums[i] <= 10^4.
"""

def maximumUniqueSubarray(nums):
    start = end = 0
    numSet = set()
    maxScore = currScore = 0

    while end < len(nums):
        if nums[end] not in numSet:
            numSet.add(nums[end])
            currScore += nums[end]
            maxScore = max(maxScore, currScore)
            end += 1
        else:
            numSet.remove(nums[start])
            currScore -= nums[start]
            start += 1
    
    return maxScore