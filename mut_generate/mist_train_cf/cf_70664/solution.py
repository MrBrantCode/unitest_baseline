"""
QUESTION:
Given a set of distinct positive integers `nums`, create a function `largestDivisibleSubset(nums)` that returns the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies `answer[i] % answer[j] == 0` or `answer[j] % answer[i] == 0`. The subset must contain the smallest and largest number from the original set. If there are multiple solutions, return any of them. The function should work for `1 <= nums.length <= 1000` and `1 <= nums[i] <= 2 * 10^9`.
"""

def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []

    nums.sort()
    result = [[num] for num in nums]
    max_length = 1
    max_idx = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(result[i]) < len(result[j]) + 1:
                result[i] = result[j] + [nums[i]]
        if len(result[i]) > max_length:
            max_length = len(result[i])
            max_idx = i

    return result[max_idx]