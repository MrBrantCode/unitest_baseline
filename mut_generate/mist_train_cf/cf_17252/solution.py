"""
QUESTION:
Design an algorithm to find the index of the longest string in a given list with the following restrictions: 
- The algorithm should have a time complexity of O(n), where n is the length of the list.
- The algorithm should have a space complexity of O(1), meaning it should use a constant amount of additional space regardless of the size of the input list.
"""

def entrance(lst):
    max_length = 0
    max_index = 0
    
    for i in range(len(lst)):
        if len(lst[i]) > max_length:
            max_length = len(lst[i])
            max_index = i
            
    return max_index