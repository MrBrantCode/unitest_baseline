"""
QUESTION:
Write a function named `extract_item_at_index_2` that takes a list as input and returns the item at index 2 without using built-in list indexing or slicing methods. Use a loop and basic list manipulation techniques to implement the function.
"""

def extract_item_at_index_2(lst):
    item_at_index_2 = None
    counter = 0

    for item in lst:
        if counter == 2:
            item_at_index_2 = item
            break
        counter += 1

    return item_at_index_2