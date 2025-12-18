"""
QUESTION:
Write a function named "common" that takes any number of lists as input. The function should return a list of common elements among all input lists. The returned list should be sorted in ascending order and should not contain any duplicate elements. The function should not use any built-in Python list functions for sorting and removing duplicates.
"""

def remove_duplicates(mylist: list):
    result = []
    for i in mylist:
        if i not in result:
            result.append(i)
    return result

def custom_sort(mylist: list):
    n = len(mylist)
    for i in range(n):
        for j in range(0, n-i-1):
            if mylist[j] > mylist[j + 1] :
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist

def common(*args):
    common_elements = []

    for i in args[0]:
        if all(i in list for list in args) and i not in common_elements:
            common_elements.append(i)
    
    common_elements = remove_duplicates(common_elements)
    common_elements = custom_sort(common_elements)

    return common_elements