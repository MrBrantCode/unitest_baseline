"""
QUESTION:
Write a Python function `unique_elements` that takes two lists of integers `list1` and `list2` and returns a new list containing only the unique elements from both lists, sorted in ascending order. The function should handle up to 1,000,000 elements in each list, with integers ranging from -1,000,000 to 1,000,000, and have a time complexity no greater than O(n log n).
"""

def unique_elements(list1, list2):
    # Use the set data type to remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    # Find the unique elements between the two sets
    unique_set = set1 ^ set2

    # Convert back to a list and sort
    unique_list = sorted(list(unique_set))

    return unique_list