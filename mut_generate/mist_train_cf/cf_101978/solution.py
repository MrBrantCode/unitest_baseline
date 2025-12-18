"""
QUESTION:
Write a function `find_top_k_product(nums, k)` that takes a list of integers `nums` and an integer `k` as input, calculates the product of the top-k elements in the list based on their probabilities (defined as each element's value divided by the sum of all elements), and returns the product. The function should assume that the input list contains at least k elements and that k is a positive integer.
"""

def find_top_k_product(nums, k):
    total_sum = sum(nums)
    probabilities = [num / total_sum for num in nums]
    sorted_nums = sorted(nums, key=lambda x: probabilities[nums.index(x)], reverse=True)
    top_k_nums = sorted_nums[:k]
    product = 1
    for num in top_k_nums:
        product *= num
    return product