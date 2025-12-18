"""
QUESTION:
Write a function `merge_lists(list1, list2)` that merges two given lists of equal size into the first list in-place, such that the resulting list contains alternating elements from the two lists. The function should not use any additional memory to create a new list. It should modify the first list in-place to achieve the desired result, with a time complexity of O(n), where n is the size of the input lists.
"""

def merge_lists(list1, list2):
    # Check if the lists are empty
    if len(list1) == 0 or len(list2) == 0:
        return list1 + list2
    
    # Initialize the pointers for both lists
    pointer1 = 0
    pointer2 = 0
    
    # Iterate through the first list
    while pointer1 < len(list1):
        # Check if pointer2 is out of bounds
        if pointer2 >= len(list2):
            break
        
        # Insert the element from list2 into list1 at the appropriate position
        list1.insert(pointer1 + 1, list2[pointer2])
        
        # Increment the pointers
        pointer1 += 2
        pointer2 += 1
    
    return list1