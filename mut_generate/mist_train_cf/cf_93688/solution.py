"""
QUESTION:
Design a function `find_common_elements` that compares two sorted lists and returns a list with the common elements and their indices in both lists. The function should implement its own algorithm for finding the common elements and their indices without using any built-in functions or libraries for searching or comparing elements in the lists. The function should handle duplicate elements and count them multiple times based on their occurrences in both lists. The function should take two parameters: `list_one` and `list_two`, both of which are sorted lists of integers. The function should return three values: a list of common elements, a list of indices of the common elements in `list_one`, and a list of indices of the common elements in `list_two`.
"""

def find_common_elements(list_one, list_two):
    common_elements = []
    indices_list_one = []
    indices_list_two = []
    i = 0
    j = 0
    
    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            i += 1
        elif list_one[i] > list_two[j]:
            j += 1
        else:
            common_elements.append(list_one[i])
            indices_list_one.append(i)
            indices_list_two.append(j)
            i += 1
            j += 1
    
    return common_elements, indices_list_one, indices_list_two