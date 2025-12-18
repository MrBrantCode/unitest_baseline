"""
QUESTION:
Write a function called `insert_sorted` that takes a list `lst`, an `item`, and a `position` as parameters. The function should sort the list if it's not already sorted, then insert the item at the specified position. If the position is out of bounds (either negative or greater than the length of the list), the function should return an error message. The function should return the modified list.
"""

def insert_sorted(lst, item, position):
    # Check if position is out of bounds
    if position < 0 or position > len(lst):
        return "Position is out of bounds"
    
    # Sort the list if it's not already sorted
    if not sorted(lst) == lst:
        lst.sort()
    
    # Insert the item at the specified position
    lst.insert(position, item)
    
    return lst