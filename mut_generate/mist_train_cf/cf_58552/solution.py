"""
QUESTION:
Write a function named `find_common` that takes three sorted lists as input and returns a list of common elements among them without using built-in methods or data structures like sets and dictionaries. The function should handle negative elements, zeros, and lists of different lengths, and ensure that the returned list contains unique elements.
"""

def find_common(list1, list2, list3):
    common_elements = []
    for i in list1:
        exists_list_2 = False
        exists_list_3 = False
        
        for j in list2:
            if i == j:
                exists_list_2 = True
                break
        
        if exists_list_2:
            for k in list3:
                if i == k:
                    exists_list_3 = True
                    break
        
        if exists_list_2 and exists_list_3 and i not in common_elements:
            common_elements.append(i)
    
    return common_elements