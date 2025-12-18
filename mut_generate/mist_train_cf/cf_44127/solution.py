"""
QUESTION:
Write a function `mergeSortedList` that takes two sorted lists, `list1` and `list2`, as input. `list1` contains only negative numbers in ascending order and `list2` contains only non-negative numbers in ascending order. The function should return a new sorted list where all negative numbers from `list1` are placed first in descending order, followed by the non-negative numbers from `list2`. The function should not use any built-in sorting functions.
"""

def mergeSortedList(list1, list2):
    sortedList = []
    len1 = len(list1)
    len2 = len(list2)
    i = 0
    j = 0

    while(i < len1 and j < len2):
        if list1[i] < 0 and list1[i] > list2[j]:
            sortedList.append(list1[i])
            i += 1
        else:
            sortedList.append(list2[j])
            j += 1

    while(i < len1):
        sortedList.append(list1[i])
        i += 1

    while(j < len2):
        sortedList.append(list2[j])
        j += 1

    return sortedList