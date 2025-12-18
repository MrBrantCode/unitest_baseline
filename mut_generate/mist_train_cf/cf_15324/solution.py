"""
QUESTION:
Implement a function `remove_duplicates(nums)` that takes a list of integers as input and returns a new list with duplicates removed, without using any built-in Python functions or libraries. The function should have a time complexity of O(n log n) or better.
"""

def entance(nums):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(nums, left, right)

    def merge(nums, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    merge_sort(nums)
    result = []

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            result.append(nums[i])

    return result