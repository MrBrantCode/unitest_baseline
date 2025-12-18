"""
QUESTION:
Write a function `product_except_self` that takes a list of numbers as input and returns a list of numbers where each element at index `i` is the product of all numbers in the input list except the number at index `i`. The input list will not contain any zeros.
"""

def product_except_self(nums):
    length = len(nums)
    prefix = [1] * length
    suffix = [1] * length

    # Calculate prefix products
    for i in range(1, length):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Calculate suffix products
    for i in range(length-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # Calculate result
    result = [0] * length
    for i in range(length):
        result[i] = prefix[i] * suffix[i]

    return result