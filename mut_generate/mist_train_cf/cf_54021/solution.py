"""
QUESTION:
Write a function named `find_max` that takes three lists of numbers as parameters and returns a tuple of the maximum numbers from each list. The function must handle cases where the inputs are not lists, empty lists, or lists containing non-numeric values.
"""

def find_max(nums1, nums2, nums3):
    # Ensure that inputs are all lists
    if not (isinstance(nums1, list) and isinstance(nums2, list) and isinstance(nums3, list)):
        return "Error: All inputs must be of list type."
    # Ensure that lists are not empty
    if not (nums1 and nums2 and nums3):
        return "Error: No empty lists are allowed."
    # Ensure that lists contain only numbers (integers and/or floats)
    for lst in [nums1, nums2, nums3]:
        for i in lst:
            if not (isinstance(i, int) or isinstance(i, float)):
                return "Error: All list elements must be numbers."
    # Calculate max for each list and return tuple of results
    return (max(nums1), max(nums2), max(nums3))