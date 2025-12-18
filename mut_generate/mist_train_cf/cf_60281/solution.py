"""
QUESTION:
Develop a function `find_common_elements` that takes three sorted arrays `list1`, `list2`, and `list3` as input and returns a list of common elements among them. The function should achieve O(n) time complexity where n is the total number of elements in all arrays and should not use any built-in methods for finding common elements.
"""

def find_common_elements(list1, list2, list3):
    index1 = index2 = index3 = 0
    common_elements = []

    while index1 < len(list1) and index2 < len(list2) and index3 < len(list3):
        if list1[index1] == list2[index2] == list3[index3]:
            common_elements.append(list1[index1])
            index1 += 1
            index2 += 1
            index3 += 1
            
        else:
            min_value = min(list1[index1], list2[index2], list3[index3])
            
            if list1[index1] == min_value:
                index1 += 1
                
            if list2[index2] == min_value:
                index2 += 1
                
            if list3[index3] == min_value:
                index3 += 1

    return common_elements