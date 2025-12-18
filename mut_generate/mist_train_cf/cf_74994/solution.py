"""
QUESTION:
Create a function named `merged_list` that takes two lists `list1` and `list2` as input, merges them into a single list, removes any duplicate elements, and sorts the resulting list in descending order without using Python's built-in `merge` and `sort` functions.
"""

def merged_list(list1: list, list2: list):
    # Create a new list by merging the two input lists
    merged = list1 + list2
    # Use set to remove duplicate elements
    unique = list(set(merged))
    # Use bubble sort to sort the list in descending order
    for i in range(len(unique)):
        for j in range(len(unique) - 1):
            if unique[j] < unique[j + 1]:
                # Swap elements if the current element is less than the next element
                unique[j], unique[j + 1] = unique[j + 1], unique[j]
    return unique