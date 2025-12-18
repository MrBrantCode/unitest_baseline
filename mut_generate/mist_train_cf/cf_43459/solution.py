"""
QUESTION:
Write a function `max_two_subarray_product(nums)` that takes an array of integers as input and returns the maximum product of any two non-overlapping subarrays within the array. The subarrays should not share any common elements, meaning if one subarray ends at index `i`, the other subarray should start from index `i+2` or later.
"""

def max_two_subarray_product(nums):
    if len(nums) < 2:
        return None

    max_product = [0] * len(nums)
    min_product = [0] * len(nums)
    max_product[0] = min_product[0] = nums[0]
    max_prod_2_subarr = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product[i] = max(min_product[i-1] * nums[i], nums[i])
            min_product[i] = min(max_product[i-1] * nums[i], nums[i])
        else:
            max_product[i] = max(max_product[i-1] * nums[i], nums[i])
            min_product[i] = min(min_product[i-1] * nums[i], nums[i])
        max_prod_2_subarr = max(max_prod_2_subarr, max_product[i])

    right_max = [0] * len(nums)
    right_max[-1] = max_product[-1]
    for i in range(len(nums)-2, -1, -1):
        right_max[i] = max(right_max[i+1], max_product[i])

    ans = float('-inf')
    for i in range(0, len(nums) - 2):
        ans = max(ans, max_product[i] * right_max[i+2])

    return ans