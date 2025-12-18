"""
QUESTION:
Create a function `common_elements(list1, list2)` that takes two sorted lists as input and returns a list of elements common to both input lists without using any built-in methods. The input lists are guaranteed to be sorted and may contain distinct, non-consecutive elements.
"""

def common_elements(list1, list2):
    i, j = 0, 0
    common = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return common