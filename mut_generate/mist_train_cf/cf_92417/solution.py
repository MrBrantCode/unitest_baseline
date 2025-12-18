"""
QUESTION:
Write a function `get_unique_elements(lst)` that calculates the number of unique elements in a given list `lst`. The function should have a time complexity of O(n) and must not use any additional data structures.
"""

def get_unique_elements(lst):
    # Sort the list in place
    lst.sort()

    # Initialize a variable to keep track of the number of unique elements
    count = 0

    # Iterate over the list
    for i in range(len(lst)):
        # Check if the current element is the same as the next element
        # If they are different, increment the count
        if i == len(lst) - 1 or lst[i] != lst[i+1]:
            count += 1

    return count