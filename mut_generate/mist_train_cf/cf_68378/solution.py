"""
QUESTION:
Merge two pre-sorted lists into a single sorted list without using built-in sort functionality.

Write a function named `merge_sorted_lists` that takes two arguments, `list1` and `list2`, both of which are pre-sorted lists of elements that can be compared. The function should return a new list that contains all elements from both input lists, sorted in ascending order.
"""

def merge_sorted_lists(list1, list2):
    result = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1[0])
            list1.pop(0)
        else:
            result.append(list2[0])
            list2.pop(0)
    if len(list1) > 0:
        result += list1
    if len(list2) > 0:
        result += list2
    return result