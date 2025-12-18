"""
QUESTION:
Create a function called `productExceptSelf` that calculates the product of all elements in a list of integers and returns a new list where each element is the product of all the numbers in the original list except the one at the same index. The function must not use the division operation and must have a time complexity of O(n), where n is the length of the list.
"""

def productExceptSelf(nums):
    size = len(nums)
    output = [1] * size
    left = [1] * size
    right = [1] * size

    for i in range(1, size):
        left[i] = nums[i - 1] * left[i - 1]

    for i in reversed(range(size - 1)):
        right[i] = nums[i + 1] * right[i + 1]

    for i in range(size):
        output[i] = left[i] * right[i]

    return output