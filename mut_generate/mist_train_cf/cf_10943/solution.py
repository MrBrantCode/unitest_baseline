"""
QUESTION:
Implement a function `find_median` that takes a list of integers as input and returns the median of the list. The function should use a sorting algorithm (such as bubble sort or insertion sort) to sort the list in ascending order, and then find the middle element. The function should handle lists with an odd number of elements, where the middle element is the median, and lists with an even number of elements, where the median is the average of the two middle elements.
"""

def find_median(nums):
    """
    This function finds the median of a list of integers.
    
    It first sorts the list using the bubble sort algorithm, then finds the middle element.
    If the list has an odd number of elements, the middle element is the median.
    If the list has an even number of elements, the median is the average of the two middle elements.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    float: The median of the list.
    """

    # Make a copy of the list to avoid modifying the original list
    nums_copy = nums.copy()

    # Perform bubble sort
    n = len(nums_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_copy[j] > nums_copy[j + 1]:
                nums_copy[j], nums_copy[j + 1] = nums_copy[j + 1], nums_copy[j]

    # Find the median
    if n % 2 == 1:
        # If the list has an odd number of elements, the middle element is the median
        median = nums_copy[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle elements
        mid1 = nums_copy[n // 2 - 1]
        mid2 = nums_copy[n // 2]
        median = (mid1 + mid2) / 2

    return median