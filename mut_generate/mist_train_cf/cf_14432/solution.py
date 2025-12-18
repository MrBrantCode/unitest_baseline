"""
QUESTION:
Write a function `find_median(nums)` that takes a list of numbers with an odd number of elements as input and returns the median without using any built-in functions or libraries that directly calculate the median. The input list is guaranteed to have an odd number of elements.
"""

def find_median(nums):
    # Sort the list in ascending order
    sorted_nums = bubble_sort(nums)

    # Find the middle index
    mid_index = (len(sorted_nums) - 1) // 2

    # Return the number at the middle index
    return sorted_nums[mid_index]


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums