"""
QUESTION:
Write a function `calculate_median` that takes a list of integers as input and returns the median. The function must sort the list and calculate its length without using built-in sorting functions or the `len()` function.
"""

def calculate_median(nums):
    # Implement a sorting algorithm to sort the list in ascending order
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    # Calculate the length of the list without using len()
    n = 0
    for _ in nums:
        n += 1

    if n % 2 == 0:
        # if the length of the list is even, take the average of the middle two elements
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        # if the length of the list is odd, take the middle element
        median = nums[n // 2]
    
    return median