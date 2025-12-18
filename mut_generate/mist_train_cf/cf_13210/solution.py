"""
QUESTION:
Create a function `common_elements(list1, list2)` that finds the common elements between two sorted lists `list1` and `list2` with a time complexity of O(n) and a space complexity of O(1), where n is the length of the longer list.
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