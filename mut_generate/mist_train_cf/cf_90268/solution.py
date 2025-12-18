"""
QUESTION:
Write a function `find_median` that calculates the median of a given list of integers. The list may contain any number of elements and may not be sorted. The function should return the median as a floating point number if the list has an even number of elements, and an integer if the list has an odd number of elements.
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