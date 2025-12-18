"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that takes two lists as input, removes duplicates, and returns the common elements between the two lists in descending order. The function should be able to handle lists containing integers, floats, or strings, with a maximum length of 10,000 elements, and have a time complexity of O(nlogn), where n is the total number of elements in both lists.
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