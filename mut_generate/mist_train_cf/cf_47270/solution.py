"""
QUESTION:
Write a function called `find_smallest_missing_positive(nums)` that, given a list of integers `nums`, finds the smallest missing positive integer in the list. The function should handle edge cases where the list may include duplicate entries, negative numbers, zeros, or be in a non-sequential order. The function must perform this task in O(n) time complexity and use O(1) additional space, excluding the input list's space.
"""

def find_smallest_missing_positive(nums):
    if not nums:
        return 1

    n = len(nums)
    contains_one = 1 in nums
    if not contains_one:
        return 1

    if n == 1:
        return 2

    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    for i in range(n):
        a = abs(nums[i])
        if a == n:
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])

    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1