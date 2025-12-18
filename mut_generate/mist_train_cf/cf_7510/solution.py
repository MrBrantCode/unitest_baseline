"""
QUESTION:
Implement a function `combine_sorted_lists(list1, list2)` to combine two sorted lists into a single sorted list without any duplicate elements. The function should handle lists of any length and size, including edge cases where one or both lists are empty. The time complexity should be O(n+m), where n and m are the lengths of `list1` and `list2` respectively. Do not use any built-in functions or methods for removing duplicate elements from the final list.
"""

def combine_sorted_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if not result or list1[i] != result[-1]:
                result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            if not result or list1[i] != result[-1]:
                result.append(list1[i])
            i += 1
        else:
            if not result or list2[j] != result[-1]:
                result.append(list2[j])
            j += 1

    # Add remaining elements of list1, if any
    while i < len(list1):
        if not result or list1[i] != result[-1]:
            result.append(list1[i])
        i += 1

    # Add remaining elements of list2, if any
    while j < len(list2):
        if not result or list2[j] != result[-1]:
            result.append(list2[j])
        j += 1

    return result