"""
QUESTION:
Write a function `compute_max_difference(list1, list2)` that calculates the maximum absolute difference between two lists of numbers. The function should ignore duplicates in the lists and consider only unique numbers when calculating the maximum absolute difference.
"""

def compute_max_difference(list1, list2):
    unique_nums1 = set(list1)
    unique_nums2 = set(list2)
    max_diff = None
    for num1 in unique_nums1:
        for num2 in unique_nums2:
            diff = abs(num1 - num2)
            if max_diff is None or diff > max_diff:
                max_diff = diff
    return max_diff