"""
QUESTION:
Write a function `find_kth_largest` that takes a list of integers `nums` and an integer `k` as input, and returns the `k`th largest element in `nums`. The function should handle cases where `k` is larger than the size of `nums`, in which case it should return an error message. The list `nums` may contain duplicates and negative numbers. The index is 0-based, so the `k`th largest element is at index `k-1`.
"""

def find_kth_largest(nums, k):
    """
    This function finds the kth largest element in a given list of integers.
    
    Args:
    nums (list): A list of integers.
    k (int): The position of the number to be found.
    
    Returns:
    int: The kth largest number in the list, or an error message if k is larger than the size of the list.
    """
    nums.sort(reverse=True) # Sorting the list in descending order
    if k > len(nums): # If k is bigger than the size of the list
        return "k is bigger than the size of the list"
    else: 
        return nums[k-1] # Return the kth largest number