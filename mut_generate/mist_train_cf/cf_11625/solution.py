"""
QUESTION:
Create a function `find_median` that takes a list of integers as input and returns the median of the list. The input list can have up to 10^5 elements, may contain duplicate elements, and the elements can range from -10^9 to 10^9. The function should have a time complexity of O(nlogn) or better and a space complexity of O(1) or better.
"""

def find_median(nums):
    """
    This function calculates the median of a given list of integers.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    float: The median of the input list.
    """
    
    # Sort the input list in ascending order
    nums.sort()
    
    # Calculate the length of the input list
    n = len(nums)
    
    # Calculate the index of the middle element
    mid = n // 2
    
    # If the number of elements is odd, return the middle element as the median
    if n % 2 != 0:
        return nums[mid]
    
    # If the number of elements is even, return the average of the two middle elements as the median
    else:
        return (nums[mid - 1] + nums[mid]) / 2