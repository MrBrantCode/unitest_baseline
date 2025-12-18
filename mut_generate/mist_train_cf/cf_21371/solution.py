"""
QUESTION:
Create a function called merge_sorted_lists that takes two sorted lists of integers as input and returns a new list containing all elements from both lists in descending order. The function should not use any built-in sorting functions and should have a time complexity of O(n), where n is the total number of elements in both lists. It should also have a space complexity of O(1) and should be implemented using a single while loop, without using any nested loops or recursion.
"""

def merge_sorted_lists(list_1, list_2):
    result = []
    i = len(list_1) - 1
    j = len(list_2) - 1
    
    while i >= 0 and j >= 0:
        if list_1[i] >= list_2[j]:
            result.append(list_1[i])
            i -= 1
        else:
            result.append(list_2[j])
            j -= 1
    
    while i >= 0:
        result.append(list_1[i])
        i -= 1
    
    while j >= 0:
        result.append(list_2[j])
        j -= 1
    
    return result