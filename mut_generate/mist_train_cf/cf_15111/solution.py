"""
QUESTION:
Find a duplicate in an array of integers in the range [0, n) using the function `find_duplicate(nums)` without using any additional data structures. The function should handle duplicate elements in the array, have a time complexity of O(n), and a space complexity of O(1). The function takes a list of integers `nums` as input and returns the duplicate element if found, otherwise returns -1.
"""

def find_duplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1