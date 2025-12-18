"""
QUESTION:
Write a function named `find_common_items` that takes two lists `list1` and `list2` as input and returns a new list containing the common items between the two lists. The function should handle lists of any length and the items in the lists can be of any data type. The function should not include duplicate items in the output list if there are duplicate items in the input lists.
"""

def find_common_items(list1, list2):
    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items