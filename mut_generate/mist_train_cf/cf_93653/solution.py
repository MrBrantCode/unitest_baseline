"""
QUESTION:
Create a function `remove_duplicates(nums)` that takes a list of integers as input and returns a new list with all duplicates removed. The function should have a time complexity of O(n log n) or better. The implementation should be from scratch without using any built-in Python functions or libraries. The input list may contain duplicate integers in any order. The output list should contain the unique integers in ascending order.
"""

def remove_duplicates(nums):
    # Step 1: Sort the list using mergesort algorithm
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

    # Step 1: Sort the list using mergesort algorithm
    merge_sort(nums)

    # Step 2: Initialize an empty list for unique integers
    result = []

    # Step 3: Iterate over the sorted list and add unique integers to result
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            result.append(nums[i])

    # Step 4: Return the list without duplicates
    return result