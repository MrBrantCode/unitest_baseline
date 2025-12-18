"""
QUESTION:
Insert a new element into a sorted array with a time complexity of O(log n). The function should not use any built-in sorting functions or libraries. The array is 0-indexed and can contain duplicate values. The function should shift elements to the right to accommodate the new element.
"""

def insert_into_sorted_array(nums, target):
    """
    Inserts a new element into a sorted array with a time complexity of O(log n).
    
    Args:
    nums (list): A sorted list of integers.
    target (int): The new element to be inserted into the sorted list.
    
    Returns:
    list: The updated list with the new element inserted.
    """
    
    # Initialize start and end pointers
    start, end = 0, len(nums) - 1
    
    # Repeat steps until start is less than or equal to end
    while start <= end:
        # Calculate the middle index
        mid = (start + end) // 2
        
        # If the new element is equal to the element at mid index, insert the new element at mid index
        if nums[mid] == target:
            nums.insert(mid, target)
            return nums
        
        # If the new element is less than the element at mid index, set end as mid - 1
        elif nums[mid] > target:
            end = mid - 1
        
        # If the new element is greater than the element at mid index, set start as mid + 1
        else:
            start = mid + 1
    
    # If start becomes greater than end and the new element has not been inserted, 
    # it means the new element should be inserted at the index start
    nums.insert(start, target)
    
    return nums