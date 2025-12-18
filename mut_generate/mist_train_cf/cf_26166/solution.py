"""
QUESTION:
Design a function named `find_median` that takes two sorted lists of integers as input and returns the median of the combined lists. The function should be able to handle lists of any length, including lists with an even or odd number of elements.
"""

def find_median(nums1, nums2):
    """
    This function takes two sorted lists of integers as input and returns the median of the combined lists.

    Args:
    nums1 (list): The first sorted list of integers.
    nums2 (list): The second sorted list of integers.

    Returns:
    float: The median of the combined lists.
    """
    # Combine the two lists into one list
    combined = []
    i, j = 0, 0

    # Merge the two lists while maintaining sorted order
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            combined.append(nums1[i])
            i += 1
        else:
            combined.append(nums2[j])
            j += 1

    # If there are remaining elements in either list, append them to the combined list
    while i < len(nums1):
        combined.append(nums1[i])
        i += 1
    while j < len(nums2):
        combined.append(nums2[j])
        j += 1

    # Calculate the median
    n = len(combined)
    if n % 2 == 0:
        # If the length is even, the median is the average of the two middle numbers
        median = (combined[n // 2 - 1] + combined[n // 2]) / 2
    else:
        # If the length is odd, the median is the middle number
        median = combined[n // 2]

    return median