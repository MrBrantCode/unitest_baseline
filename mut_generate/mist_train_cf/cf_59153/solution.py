"""
QUESTION:
Design an efficient function called "optimize_algorithm" that takes an input list of integers and returns the sorted list using the most efficient sorting algorithm. Ensure the function has a time complexity of O(n log n) and minimize space complexity.
"""

def optimize_algorithm(nums):
    """
    This function sorts a list of integers using the merge sort algorithm.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A sorted list of integers.
    """
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = optimize_algorithm(nums[:mid])
    right_half = optimize_algorithm(nums[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # If there are remaining elements in either half, append them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged