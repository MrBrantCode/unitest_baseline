"""
QUESTION:
Create a function `smallest_absent_integer` that takes an array of integers as input and returns the smallest positive integer that is not present in the array. The function should have a computational complexity of O(n) and a space complexity of O(1). The array may contain negative numbers, zeros, and duplicate numbers, and the function should handle these cases.
"""

def smallest_absent_integer(nums):
    if not nums:      # If array is empty (boundary case)
        return 1
      
    nums = set(nums)  # Remove duplicate numbers
    nums = [i for i in nums if i > 0]  # Remove negative numbers and zero

    if not nums:     # If array contained only negative numbers and/or zeros (boundary case)
        return 1
      
    n = len(nums)
    nums = sorted(nums)  # Sort the positive integers in ascending order

    if nums[0] != 1 :  # If the smallest integer is not 1
        return 1
    elif n == 1:  # If there is only 1 positive integer and it is 1
        return 2

    for i in range(n - 1):
        # If the difference between two adjacent numbers is more than 1,
        # return the first number + 1
        if nums[i + 1] - nums[i] > 1:  
            return nums[i] + 1

    return nums[-1] + 1  # If no absent positive integers found in the array, return the largest number + 1