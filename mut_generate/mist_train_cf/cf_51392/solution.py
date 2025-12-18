"""
QUESTION:
Write a recursive function `find_smallest` that finds the smallest integer in a nested list and returns it along with its index. If the smallest integer appears multiple times, return the index of the first occurrence. If the list or any sub-list is empty, return -1. Do not use built-in functions like `min()` or `index()`. The function should take a list as input and return a tuple containing the smallest integer and its index.
"""

def find_smallest(lst, smallest=float('inf'), index=-1, curr_index=0):
    for i in range(len(lst)):
        item = lst[i]
        if isinstance(item, list):
            smallest, index = find_smallest(item, smallest, index, curr_index+i)
        else:
            curr_index += i
            if item<smallest:
                smallest = item
                index = curr_index
    return smallest, index if smallest!=float('inf') else -1