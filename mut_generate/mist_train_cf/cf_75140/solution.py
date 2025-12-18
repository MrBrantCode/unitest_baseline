"""
QUESTION:
Implement a function called `linear_search` that takes a list and a target value as input, and returns the index of the target value in the list if it exists, or `None` otherwise. The function should iterate over the list to find the target value. The list is not guaranteed to be sorted.
"""

def linear_search(lst, target):
    # Step 1: Iterate over the list
    for i in range(0, len(lst)):
        # Step 2: Check if current element matches the target
        if lst[i] == target:
            return i  # Return the index of the match
    return None  # Return None if no match found