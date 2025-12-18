"""
QUESTION:
Write a function `insert_item_at_index(lst, item, index)` that inserts a new item into a given list `lst` at the specified `index`, with the following restrictions:
- The function must ensure that the `index` is within the valid range of the list's length (i.e., 0 <= index <= len(lst)).
- If the `index` is out of bounds, the function must return an error message.
- The function must check if the `item` to be inserted is already present in the list, and if so, it must not insert it again and return an error message instead.
- The function must handle duplicate elements in the list correctly, ensuring that the new item is inserted at the specified index even if there are multiple occurrences of the same item.
- The time complexity of the function must be O(n), where n is the length of the list.
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