"""
QUESTION:
Write a function named `insert_tuple` that inserts an item at a specific index in a tuple. The function should take three parameters: the input tuple, the index at which the item should be inserted, and the item to be inserted. Since tuples are immutable, the function should return a new tuple with the item inserted, rather than modifying the original tuple.
"""

def insert_tuple(tup, index, item):
    """
    Inserts an item at a specific index in a tuple.

    Args:
        tup (tuple): The input tuple.
        index (int): The index at which the item should be inserted.
        item (any): The item to be inserted.

    Returns:
        tuple: A new tuple with the item inserted.
    """
    temp_list = list(tup)   # convert tuple to list
    temp_list.insert(index, item)   # insert item to list at index
    return tuple(temp_list)   # convert list back to tuple