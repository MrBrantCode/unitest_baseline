"""
QUESTION:
Implement the function `find_duplicate(nums)` that finds the first duplicate in the given array `nums`, where each element is in the range `[0, n-1]` and `n` is the length of the array. The function should return the first duplicate if found, and -1 otherwise. The solution must handle the case where the array contains duplicate elements, have a time complexity of O(n), and a space complexity of O(1), without using any additional data structures.
"""

def find_duplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1