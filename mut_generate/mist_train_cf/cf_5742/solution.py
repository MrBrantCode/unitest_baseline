"""
QUESTION:
Write a function `find_kth_largest` that finds the kth largest element in a list of integers. The function should exclude any elements that are more than two standard deviations away from the mean of the list and return `None` if the list is empty, contains less than k elements, or if there are no elements after excluding outliers.
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