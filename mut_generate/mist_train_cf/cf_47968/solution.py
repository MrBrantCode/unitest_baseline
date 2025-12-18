"""
QUESTION:
Implement a stable sorting algorithm that can efficiently sort data in different types (numerical, alphabetical, chronological order) while maintaining the original sequence of equal elements. The algorithm should be able to handle various data types and ensure that the relative order of equal elements remains consistent with their original order in the input data.
"""

def stable_sort(data):
    """
    This function performs a stable merge sort on a given list of data.
    
    Args:
        data (list): A list of elements to be sorted.
        
    Returns:
        list: A sorted list of elements.
    """
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left_half = stable_sort(data[:mid])
    right_half = stable_sort(data[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    """
    This function merges two sorted lists into one sorted list.
    
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
        
    Returns:
        list: A merged sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged