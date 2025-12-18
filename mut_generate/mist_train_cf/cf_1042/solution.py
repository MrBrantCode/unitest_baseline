"""
QUESTION:
Write a function `countItems` that takes a hashmap as input and returns the number of items in the hashmap. The function must use a recursive approach with backtracking and cannot use any built-in functions or methods for counting the items, loops, recursion with iteration, or any other form of iteration to traverse the hashmap.
"""

def countItems(hashmap):
    if not hashmap:  # Base case: hashmap is empty
        return 0

    _, _ = hashmap.popitem()  # Remove one key-value pair using backtracking
    count = 1  # Increment count by 1

    return count + countItems(hashmap)  # Recursive call with updated hashmap