"""
QUESTION:
Implement a function `arr_cumu_product(nums)` that takes an array of integers as input and returns an array where each element at the i'th position is the cumulative product of all elements in the input array excluding the element at the i'th position. The function must handle negative numbers and zeros, and maintain the original order of elements. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the output array.
"""

def arr_cumu_product(nums):
    n = len(nums)
    output = [1]*n

    # Calculate prefix product
    prefix_product = 1
    for i in range(n):
        output[i] *= prefix_product
        prefix_product *= nums[i]

    # Calculate suffix product
    suffix_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= nums[i]
    
    return output