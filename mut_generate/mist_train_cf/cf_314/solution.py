"""
QUESTION:
Create a function `add_items` that initializes an empty list and adds `n` unique items to it. The items should be generated dynamically using a for loop that iterates through a range based on the value of `n`. Each item added to the list must be unique, and if a duplicate item is encountered, it should be skipped. The function must not use any built-in Python functions or libraries to check for duplicates or perform other operations, and it should have a time complexity of O(n) and a space complexity of O(1), only using the initial empty list and the input variables.
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