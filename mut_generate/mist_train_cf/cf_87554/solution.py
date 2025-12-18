"""
QUESTION:
Write a function named `find_common_elements` that takes two sorted lists as input, `list1` and `list2`, and returns a new list containing the elements that are present in both lists. The function should have a time complexity of O(n), where n is the total number of elements in both lists, and should not use any built-in functions or methods for comparing or iterating through the lists, or any temporary variables or data structures.
"""

def find_common_elements(list1, list2):
    pointer1 = 0
    pointer2 = 0
    result = []

    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return result