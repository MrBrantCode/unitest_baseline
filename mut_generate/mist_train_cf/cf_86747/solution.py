"""
QUESTION:
Write a function `countItems` that takes a hashmap as input and returns the count of items in the hashmap. You must use a recursive function that employs a backtracking algorithm to count the items. You are not allowed to use any built-in functions or methods for counting the items, loops, recursion with iteration, or any other form of iteration to iterate through the hashmap.
"""

def countItems(hashmap):
    if not hashmap:  # Base case: hashmap is empty
        return 0

    _, _ = hashmap.popitem()  # Remove one key-value pair using backtracking
    count = 1  # Increment count by 1

    return count + countItems(hashmap)  # Recursive call with updated hashmap