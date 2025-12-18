"""
QUESTION:
Implement a function named `find_min_max` that takes a list of numbers as input and returns a tuple containing the minimum and maximum elements in the list. The function should not use any built-in functions or methods for finding the minimum and maximum, and it should have a time complexity of O(n), where n is the length of the list.
"""

def find_min_max(lst):
    # Initialize min_num and max_num with the first element
    min_num = lst[0]
    max_num = lst[0]
    
    # Iterate through the rest of the list
    for num in lst[1:]:
        # Check if the current element is smaller than min_num
        if num < min_num:
            min_num = num
        
        # Check if the current element is larger than max_num
        if num > max_num:
            max_num = num
    
    return min_num, max_num