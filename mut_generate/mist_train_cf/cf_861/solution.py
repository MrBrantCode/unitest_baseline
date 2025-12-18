"""
QUESTION:
Implement a function named `remove_duplicates` that takes a list of elements as input and returns a new list with all duplicate elements removed, preserving the original order of the elements. The function should handle cases where the input list is empty or contains only one element.
"""

def remove_duplicates(nums):
    if len(nums) < 2:
        return nums
    
    unique_elements = set()
    new_list = []
    
    for num in nums:
        if num not in unique_elements:
            unique_elements.add(num)
            new_list.append(num)
    
    return new_list