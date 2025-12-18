"""
QUESTION:
Implement a function named `quickSort` to sort a list of integers in ascending order. The function should be efficient and handle increasingly larger lists with a minimum time complexity. The integers in the list may include both positive and negative numbers. The function should return the sorted list of integers.
"""

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums.pop()
        items_greater = []
        items_lower = []

        for item in nums:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return quickSort(items_lower) + [pivot] + quickSort(items_greater)