"""
QUESTION:
Write a function `find_median` that takes a list of integers `nums` as input and returns the median of the list. The median is the middle value of a sorted list of numbers. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. Assume that the input list is non-empty and contains only integers.
"""

def find_median(nums):
    # Step 1: Sort the list in ascending order
    nums.sort()

    # Step 2: Check if the length of the list is odd or even
    length = len(nums)
    if length % 2 == 1:  # Odd length
        # Step 3: Return the middle element
        return nums[length // 2]
    else:  # Even length
        # Step 4: Calculate the average of the two middle elements
        middle1 = nums[length // 2 - 1]
        middle2 = nums[length // 2]
        return (middle1 + middle2) / 2