"""
QUESTION:
Design a function `interchange_lists(list1, list2)` that takes two lists of numbers as input, interchanges their elements while maintaining the same index for each number, and handles lists of different lengths by appending surplus values from the longer list to the shorter one. The function should return the modified lists.
"""

def interchange_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)

    # Interchange elements
    for i in range(min(len1, len2)):
        list1[i], list2[i] = list2[i], list1[i]

    # If lengths are not equal, append the remaining elements of the longer list to the shorter one
    if len1 < len2:
        list1.extend(list2[len1:])
    elif len1 > len2:
        list2.extend(list1[len2:])

    return list1, list2