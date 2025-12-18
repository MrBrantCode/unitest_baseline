"""
QUESTION:
Implement a function named `find_top_k_product` that takes a list of integers `nums` and an integer `k` as input. The function should calculate the product of the top-k elements in the list based on their probabilities, where the probability of an element is its value divided by the sum of all elements in the list. The function should return this product. The value of k is guaranteed to be less than or equal to the number of elements in the list.
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