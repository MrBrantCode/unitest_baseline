"""
QUESTION:
Write a function `productExceptSelf(nums)` that takes an array of integers `nums` as input and returns an array where each element at index `i` is the product of all elements in `nums` except for `nums[i]`. The function should operate in O(n) time complexity and not use division. The output array is not considered as extra space for the purpose of space complexity analysis. The length of `nums` is between 2 and 10^5, each element in `nums` is between -30 and 30, and the product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
"""

def productExceptSelf(nums):
    length = len(nums)

    answer = [0]*length

    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
        
    R = 1;
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer