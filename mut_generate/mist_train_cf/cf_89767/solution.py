"""
QUESTION:
Create a function `insert_item_at_index` that inserts a new item into a given list at a specified index while maintaining the original order of elements. The function should have a time complexity of O(n) and handle duplicate elements. The function should return the updated list if the insertion is successful, "Index out of bounds" if the index is outside the list's valid range, and "Item already present in the list" if the item already exists in the list.
"""

def insert_item_at_index(lst, item, index):
    if index < 0 or index > len(lst):
        return "Index out of bounds"
    
    if item in lst:
        return "Item already present in the list"
    
    lst.append(None)  # Add a placeholder at the end of the list
    
    for i in range(len(lst)-1, index, -1):
        lst[i] = lst[i-1]  # Shift elements to the right
    
    lst[index] = item  # Insert item at the specified index
    
    return lst