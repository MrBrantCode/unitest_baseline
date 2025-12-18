"""
QUESTION:
Write a function `find_common_elements(list_one, list_two)` that takes two sorted lists as input and returns a tuple of three lists: common elements, indices of common elements in `list_one`, and indices of common elements in `list_two`. The function should not use any built-in functions or libraries for searching or comparing elements in the lists and should handle duplicate elements by counting them multiple times based on their occurrences in both lists.
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