"""
QUESTION:
Write a function named `remove_occurrences` that takes an item and a list as input, and returns the modified list with all occurrences of the given item removed, while maintaining the relative order of the remaining items. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1), meaning it should not use any additional data structures.
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