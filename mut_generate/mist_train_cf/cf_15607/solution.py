"""
QUESTION:
Remove all occurrences of a given item from a list while maintaining the relative order of the remaining items. The function should take two parameters: the item to be removed and the list from which the item will be removed. The solution should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1), meaning no additional data structures can be used. The function should modify the original list in-place and return the modified list.
"""

def remove_occurrences(item, lst):
    i = 0
    j = 0

    while i < len(lst):
        if lst[i] != item:
            lst[j] = lst[i]
            j += 1
        i += 1

    del lst[j:]

    return lst