"""
QUESTION:
Implement a function named `correct_sort` that sorts a list of integers in descending order without using built-in or library functions. The function should work efficiently with lists containing up to 10,000 elements, including negative numbers.
"""

def correct_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums