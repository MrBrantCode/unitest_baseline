"""
QUESTION:
Create a function named `common_elements` that takes two lists of integers as input and returns a new list containing only the common elements found in both lists, without duplicates and in ascending order. The function should have a time complexity of O(n log n), where n is the total number of elements in both input lists combined, and a space complexity of O(1), excluding the space required for the output list.
"""

def entance(list_1, list_2):
    common_elements_set = set()

    list_1.sort()
    list_2.sort()

    i, j = 0, 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] == list_2[j]:
            common_elements_set.add(list_1[i])
            i += 1
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        else:
            j += 1

    return sorted(list(common_elements_set))