"""
QUESTION:
Given a list of non-negative integers representing power values and an integer `powerlimit`, implement a function `max_contiguous_subarray_length` that returns the maximum length of a contiguous subarray where the product of all elements is less than or equal to `powerlimit`. The function should take in two parameters: a list of non-negative integers and an integer `powerlimit`, and return the maximum length of the contiguous subarray.
"""

def entrance(power, powerlimit):
    if powerlimit <= 0:
        return 0
    max_len = 0
    left = right = 0
    product = 1
    while right < len(power):
        product *= power[right]
        while product > powerlimit and left <= right:
            product /= power[left]
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len