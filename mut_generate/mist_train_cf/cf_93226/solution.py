"""
QUESTION:
Write a function named `find_median` that takes a list of numbers with an odd number of elements as input and returns the median without using any built-in functions or libraries that directly calculate the median. The input list is guaranteed to have an odd number of elements.
"""

def find_median(nums):
    # Sort the list in ascending order
    def bubble_sort(nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    # Find the middle index
    mid_index = (len(nums) - 1) // 2

    # Sort the list and return the number at the middle index
    return bubble_sort(nums)[mid_index]