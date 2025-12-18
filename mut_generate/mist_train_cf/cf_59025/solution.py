"""
QUESTION:
Write a function productExceptSelf that takes a list of integers as input and returns a list where each element at index i is the product of all the numbers in the input list except the one at index i. The function should not use division and should run in linear time complexity. The input list is 1-indexed, but the output list is 0-indexed, meaning the first element of the output corresponds to the first element of the input, and the last element of the output corresponds to the last element of the input.
"""

def productExceptSelf(nums):
    length = len(nums)
    answer = [1]*length

    for i in range(1, length):
        answer[i] = nums[i-1] * answer[i-1]
    
    R = 1

    for i in range(length-1, -1, -1):
        answer[i] *= R
        R *= nums[i]
    
    return answer