"""
QUESTION:
Create a function named `mergeSortedLists` that takes two sorted lists as arguments and returns a single sorted list without using any built-in sort function. The function should achieve optimal time complexity. The input lists are already sorted, and the function should merge them into a single sorted entity.
"""

def mergeSortedLists(list1, list2):
    i, j = 0, 0
    mergedList = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
    while i < len(list1):
        mergedList.append(list1[i])
        i += 1
    while j < len(list2):
        mergedList.append(list2[j])
        j += 1
    return mergedList