"""
QUESTION:
Delete an element from a given list at a specified index without using built-in functions or methods that access the index directly. The function should iterate through the list from the start, comparing each element to determine the index of the element to be deleted. The function must have a time complexity of O(n), where n is the number of elements before the index of the element to be deleted, and return the deleted element. The function should modify the original list in-place by shifting elements to the left to fill the gap and removing the last element.
"""

def delete_element(lst, index):
    deleted_element = None
    
    # Iterate through each element of the list
    for i in range(len(lst)):
        # Check if the current element is the one to be deleted
        if i == index:
            # Store the element to be deleted
            deleted_element = lst[i]
        elif i > index:
            # Shift elements to the left to fill the gap
            lst[i-1] = lst[i]
    
    # Remove the last element (the duplicate of the shifted element)
    lst.pop()
    
    return deleted_element