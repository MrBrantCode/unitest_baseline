"""
QUESTION:
Find a sequence of consecutive hexadecimal digits in a given set that multiply to a target product. The sequence must be a contiguous subset of the given set.
"""

def entance(nums, target):
    product = 1
    left = 0
    for right in range(len(nums)):
        product *= int(nums[right], 16)
        while product >= target:
            if product == target:
                return nums[left:right+1]
            product //= int(nums[left], 16)
            left += 1
    return []