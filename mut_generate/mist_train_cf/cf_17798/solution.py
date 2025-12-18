"""
QUESTION:
Write a function named `insert_sorted` that takes three parameters: a list `lst`, an item, and a position. The function should insert the item at the specified position in the list while ensuring the list remains sorted. If the list is not initially sorted, the function should sort it before inserting the item. The function should also handle cases where the position is out of bounds (either negative or greater than the length of the list), in which case it should return an error message.
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