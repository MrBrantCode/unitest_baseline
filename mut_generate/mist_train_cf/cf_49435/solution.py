"""
QUESTION:
Implement a function named `sorted_squares(nums)` that takes a list of integers as input and returns a new list with the squares of the input integers in ascending order. The function should handle negative numbers efficiently and run in linear time.
"""

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result