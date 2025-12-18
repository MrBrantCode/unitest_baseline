"""
QUESTION:
Create a function named `has_common_element(list1, list2)` that compares two given lists to check if they have any common element, including elements of different data types (integers, strings, booleans, and nested lists of arbitrary depth). The function should return True if there is at least one common element between the two lists, and False otherwise, with a time complexity not exceeding O(n^2), where n is the total number of elements in both lists.
"""

def has_common_element(list1, list2):
    # Convert the lists to sets for faster lookup
    set1 = set(flatten(list1))
    set2 = set(flatten(list2))
    
    # Check if there is any common element
    if set1.intersection(set2):
        return True
    else:
        return False

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item