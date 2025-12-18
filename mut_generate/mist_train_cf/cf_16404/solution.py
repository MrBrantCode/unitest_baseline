"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that generates a list of common elements from two given lists. The function should ignore duplicates, return common elements in descending order, and be able to handle lists of any length. The function should have a time complexity of O(nlogn), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    # Convert the lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    # Find the common elements
    common_elements = set1.intersection(set2)

    # Sort the common elements in descending order
    sorted_elements = sorted(common_elements, reverse=True)

    return sorted_elements