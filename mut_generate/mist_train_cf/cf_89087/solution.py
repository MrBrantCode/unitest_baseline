"""
QUESTION:
Write a function `find_kth_largest` that takes two parameters: `nums`, a list of integers, and `k`, an integer representing the kth largest element to find. The function should return the kth largest element in the list, excluding outliers that are more than two standard deviations away from the mean of the list. If the list is empty, contains less than k elements, or if there are no elements after excluding outliers, return `None`.
"""

import math

def find_kth_largest(nums, k):
    # Check for empty list or insufficient elements
    if not nums or len(nums) < k:
        return None

    # Exclude outliers
    mean = sum(nums) / len(nums)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
    threshold = mean + (2 * std_dev)
    filtered_nums = [x for x in nums if x <= threshold]

    # Sort the filtered list in descending order
    filtered_nums.sort(reverse=True)

    # Check for insufficient elements after excluding outliers
    if len(filtered_nums) < k:
        return None

    return filtered_nums[k - 1]