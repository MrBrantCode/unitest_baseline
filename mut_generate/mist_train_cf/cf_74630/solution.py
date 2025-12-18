"""
QUESTION:
Create a function `find_median_sorted_arrays` that takes two sorted lists of numbers `nums1` and `nums2` as input. The function should return the median of the combined and sorted list of numbers. The input lists are guaranteed to be sorted in ascending order.
"""

def find_median_sorted_arrays(nums1, nums2):
    """
    This function finds the median of two sorted lists of numbers.

    Args:
        nums1 (list): The first list of numbers.
        nums2 (list): The second list of numbers.

    Returns:
        float: The median of the combined and sorted list of numbers.
    """
    merged_list = sorted(nums1 + nums2)
    length = len(merged_list)
    if length % 2 == 0:
        median = (merged_list[length//2] + merged_list[length//2 - 1]) / 2
    else:
        median = merged_list[length//2]
    return median