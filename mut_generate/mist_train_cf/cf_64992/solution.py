"""
QUESTION:
Write a Python function `sort_complex_lists(list1, list2)` that sorts two given lists of complex numbers in ascending order based on their magnitude. The function should combine the two sorted lists into one sorted list without repeating the sorting process, even if the input lists are already sorted.
"""

def sort_complex_lists(list1, list2):
    list1.sort(key=lambda x: abs(x)) 
    list2.sort(key=lambda x: abs(x)) 

    merged_list = [] 
    i = j = 0 

    while i < len(list1) and j < len(list2):
        if abs(list1[i]) < abs(list2[j]):
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list