"""
QUESTION:
Create a function named `find_common_elements(list1, list2)` that takes two lists of integers as input and returns a list containing all the common elements, without any duplicates, in ascending order. The function should have a time complexity of O(n log n), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    list1.sort()
    list2.sort()
    
    common_elements = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            if len(common_elements) == 0 or list1[pointer1] != common_elements[-1]:
                common_elements.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return common_elements