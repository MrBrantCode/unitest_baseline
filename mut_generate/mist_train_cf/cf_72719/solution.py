"""
QUESTION:
Create a function `unique_BST_sort` that takes a list of mixed integers and decimals as input, and returns the list sorted in a specific order using a binary search tree (BST) methodology. The sorting sequence should start with the minimum value, followed by the maximum value of the remainder, then the minimum value not yet included, and continue with this pattern. The function should be able to handle empty lists and lists with duplicate values.
"""

def unique_BST_sort(lst):
    sorted_list = sorted(lst)
    result = []
    while sorted_list:
        result.append(sorted_list.pop(0))
        if sorted_list:
            result.append(sorted_list.pop())
    return result