"""
QUESTION:
Implement a function called `insert_items` that inserts multiple items into an array at specific positions. The function should take two parameters: an array and a list of tuples, where each tuple contains the item to be inserted and the position at which it should be inserted. If the position given is greater than the length of the array, the function should print an error message and continue with the next tuple. The function should return the modified array.
"""

def insert_items(arr, items_positions):
    for item, pos in items_positions:
        if pos > len(arr):
            print(f"Error: position {pos} is greater than the length of the array.")
            continue
        arr.insert(pos, item)
    return arr