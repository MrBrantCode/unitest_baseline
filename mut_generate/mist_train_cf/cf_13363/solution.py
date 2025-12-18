"""
QUESTION:
Implement a function `count_occurrences` that takes a list as input and returns the count of each item in the list without using built-in functions like `dict.get()` or `collections.Counter()`. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def count_occurrences(lst):
    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate over each item in the list
    for item in lst:
        # Check if the item is already in the dictionary
        if item in counts:
            # If it is, increment the count by 1
            counts[item] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            counts[item] = 1

    # Return the counts for each item
    return counts