"""
QUESTION:
Find the minimum and maximum elements in a list of numbers without using built-in functions or methods for finding the minimum and maximum. Implement a solution with a time complexity of O(n), where n is the length of the list. The function should take a list of numbers as input and return a tuple containing the minimum and maximum elements.
"""

def entrance(lst):
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