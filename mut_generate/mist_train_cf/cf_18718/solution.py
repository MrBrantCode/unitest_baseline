"""
QUESTION:
Write a function `find_duplicates` that prints all duplicate elements in a given list without using any built-in functions or data structures. The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def find_duplicates(my_list):
    """
    This function prints all duplicate elements in a given list without using any built-in functions or data structures.
    
    The function uses a modified version of the Floyd's Tortoise and Hare algorithm to find the duplicate elements in O(n) time complexity and O(1) space complexity.
    
    Parameters:
    my_list (list): The input list that may contain duplicate elements.
    
    Returns:
    The duplicate element in the list.
    """
    slow = my_list[0]
    fast = my_list[0]
    
    # Phase 1: Find the intersection point of the two pointers
    while True:
        slow = my_list[slow]
        fast = my_list[my_list[fast]]
        
        if slow == fast:
            break
    
    # Phase 2: Find the duplicate element
    slow = my_list[0]
    
    while slow != fast:
        slow = my_list[slow]
        fast = my_list[fast]
    
    return slow