"""
QUESTION:
Write a function `permute(nums)` that returns all permutations of the input array `nums` without containing any subsequence in ascending order with a length greater than 2. The function should take an array of distinct integers as input, where `1 <= nums.length <= 6` and `-10 <= nums[i] <= 10`. The output can be in any order.
"""

def permute(nums):
    def backtrack(first=0):
        if first == n:
            if subsequence_check(nums[:]):
                output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    def subsequence_check(nums):
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] < nums[i+2]:
                return False
        return True

    n = len(nums)
    output = []
    backtrack()
    return output