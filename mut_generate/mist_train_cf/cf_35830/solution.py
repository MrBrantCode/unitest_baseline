"""
QUESTION:
Create a function `productExceptSelf` that takes an array of integers `nums` as input and returns a new array where each element at index `i` is the product of all elements in `nums` except `nums[i]`. The function should have a time complexity of O(n) and should not use division.
"""

def productExceptSelf(nums):
    length = len(nums)
    ans = [1] * length
    left, right = 1, 1

    for i in range(length):
        ans[i] *= left
        ans[length - i - 1] *= right
        left *= nums[i]
        right *= nums[length - i - 1]

    return ans