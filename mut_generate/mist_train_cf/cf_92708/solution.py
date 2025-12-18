"""
QUESTION:
Create a function named `common_elements` that takes two sorted lists as input and returns a list of common elements between the two input lists. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the longer list.
"""

def common_elements(list1, list2):
    common = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            common.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return common