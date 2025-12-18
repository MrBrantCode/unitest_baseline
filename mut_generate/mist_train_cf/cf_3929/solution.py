"""
QUESTION:
Write a function named `find_common_elements` that takes two lists of integers as input and returns a new list containing their common elements. The function must have a time complexity of O(n*log(n) + m*log(m)), where n and m are the lengths of the input lists, and must not use any additional data structures besides the input lists and the output list.
"""

def find_common_elements(list1, list2):
    common_elements = []
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    index1 = 0
    index2 = 0
    while index1 < len(sorted_list1) and index2 < len(sorted_list2):
        if sorted_list1[index1] == sorted_list2[index2]:
            common_elements.append(sorted_list1[index1])
            index1 += 1
            index2 += 1
        elif sorted_list1[index1] < sorted_list2[index2]:
            index1 += 1
        else:
            index2 += 1
    return common_elements