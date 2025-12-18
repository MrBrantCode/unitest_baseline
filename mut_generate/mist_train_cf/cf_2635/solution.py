"""
QUESTION:
Write a function named `find_common_elements(list1, list2)` that takes two sorted lists as input and returns a new list containing the elements that are present in both lists. The function should not use any built-in functions or methods for comparing or iterating through the lists, and it should not use any temporary variables or data structures. The function should have a time complexity of O(n), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    # initialize pointers and result list
    pointer1 = 0
    pointer2 = 0
    result = []

    # iterate until either list reaches the end
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            # elements are equal, add to result list
            result.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            # element in list1 is smaller, increment pointer1
            pointer1 += 1
        else:
            # element in list2 is smaller, increment pointer2
            pointer2 += 1
    
    return result