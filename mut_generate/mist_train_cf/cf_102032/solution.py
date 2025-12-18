"""
QUESTION:
Implement a function `group_from_third_element` that takes a list of integers as input and returns a list of lists. The function should group the input list into sublists, starting from the third element, with each sublist containing four elements. If there are less than four elements from the third element to the end of the list, they should be grouped together as one sublist.
"""

def group_from_third_element(nums):
    start_index = 2
    groups = []
    
    if start_index + 4 <= len(nums):
        groups.append(nums[start_index:start_index + 4])
    else:
        groups.append(nums[start_index:])
        
    return groups