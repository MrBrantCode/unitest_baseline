"""
QUESTION:
Implement a function `combine_sorted_lists` that combines two sorted lists, `list1` and `list2`, into a single sorted list without any duplicate elements. The function should handle lists of any length and size, including edge cases where one or both lists are empty. The time complexity should be O(n+m), where n and m are the lengths of `list1` and `list2` respectively.
"""

def combine_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not result or list1[i] != result[-1]:
                result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not result or list2[j] != result[-1]:
                result.append(list2[j])
            j += 1
        else:
            if not result or list1[i] != result[-1]:
                result.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        if not result or list1[i] != result[-1]:
            result.append(list1[i])
        i += 1

    while j < len(list2):
        if not result or list2[j] != result[-1]:
            result.append(list2[j])
        j += 1

    return result