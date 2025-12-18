"""
QUESTION:
Write a function called `rearrange_list` that takes a list of integers as input, sorts the integers in ascending order, groups consecutive integers into sublists, and sorts duplicates in descending order within their sublists. The function should modify the input list in-place and have a time complexity of O(n log n) and a space complexity of O(1).
"""

def rearrange_list(nums):
    def partition(nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[j] == pivot:
                nums[j], nums[high] = nums[high], nums[j]
                high -= 1
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quicksort(nums, low, high):
        if low < high:
            pivot_index = partition(nums, low, high)
            quicksort(nums, low, pivot_index - 1)
            quicksort(nums, pivot_index + 1, high)

    quicksort(nums, 0, len(nums) - 1)

    i = 0
    while i < len(nums):
        start = i
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        if start != i:
            sublist = nums[start:i + 1]
            sublist.sort(reverse=True)
            nums[start:i + 1] = sublist
        i += 1