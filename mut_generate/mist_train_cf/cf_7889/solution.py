"""
QUESTION:
Design a function called find_median that takes an array of integers as input. The function should return the median of the array, defined as the middle element if the array has an odd number of elements, and the average of the two middle elements if the array has an even number of elements. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. It should also handle empty arrays, arrays with one or two elements, negative numbers, and duplicate elements correctly.
"""

def find_median(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return (nums[0] + nums[1]) / 2

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    if len(nums) % 2 == 1:
        return nums[len(nums) // 2]
    else:
        return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2