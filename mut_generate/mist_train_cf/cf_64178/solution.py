"""
QUESTION:
Write a function `max_product(nums)` that takes a list of integers as input and returns the maximum product achievable from a contiguous subsequence within the list. The subsequence must include at least one negative and one positive integer.
"""

def max_product(nums):
    if not nums:
        return 0

    max_product_ending_here = nums[0]
    min_product_ending_here = nums[0]
    max_product_so_far = nums[0]
    neg_product = float('-inf') if nums[0] < 0 else 0
    pos_product = nums[0] if nums[0] > 0 else 0

    for num in nums[1:]:
        if num > 0:
            max_product_ending_here = max(num, max_product_ending_here * num)
            min_product_ending_here = min(num, min_product_ending_here * num)
            pos_product = max(pos_product, max_product_ending_here)
            if min_product_ending_here < 0:
                neg_product = max(neg_product, min_product_ending_here)
        elif num < 0:
            temp = max_product_ending_here
            max_product_ending_here = max(num, min_product_ending_here * num)
            min_product_ending_here = min(num, temp * num)
            neg_product = max(neg_product, max_product_ending_here)
            if pos_product > 0:
                max_product_so_far = max(max_product_so_far, pos_product * neg_product)
        else:
            max_product_ending_here = 0
            min_product_ending_here = 0
            if pos_product > 0 and neg_product < 0:
                max_product_so_far = max(max_product_so_far, pos_product * neg_product)
            pos_product = neg_product = 0

        max_product_so_far = max(max_product_so_far, pos_product, neg_product)

    return max_product_so_far