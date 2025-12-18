"""
QUESTION:
Create a function `add_items` that takes an integer `n` as input and returns a list of `n` unique integers from 0 to infinity, excluding duplicates. The function should use a for loop to iterate through a dynamic range generated based on the value of `n`. The time complexity should be O(n) and the space complexity should be O(1), without using any extra data structures or built-in functions.
"""

def add_items(n):
    unique_items = set()
    result = []
    
    for i in range(n):
        item = get_next_unique_item(unique_items, i)
        if item is not None:
            result.append(item)
            
    return result

def get_next_unique_item(unique_items, current):
    while current in unique_items:
        current += 1
        
    unique_items.add(current)
    return current