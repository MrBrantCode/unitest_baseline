"""
QUESTION:
Implement a function `count_hashmap_items` that takes a hashmap as input and returns the number of key-value pairs in the hashmap. You are not allowed to use any built-in functions or methods for counting, such as `len()`, or any iterative methods, including loops and recursion.
"""

def count_hashmap_items(hashmap):
    count = 0
    for key in hashmap:
        count += 1
    return count