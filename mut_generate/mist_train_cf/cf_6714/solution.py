"""
QUESTION:
Write a recursive function find_first_occurrence that finds the index of the first occurrence of a given element in a list. The list can contain duplicate elements and the element itself can be a list. If the element is found within a sublist, return the index of the sublist. The function should have a time complexity of O(n), where n is the length of the list, and return -1 if the element is not found. The function should take three parameters: the list to search in, the element to search for, and an optional index parameter with a default value of 0.
"""

def find_first_occurrence(my_list, element, index=0):
    if index >= len(my_list):
        return -1
    
    if my_list[index] == element:
        return index
    
    if isinstance(my_list[index], list):
        sublist_index = find_first_occurrence(my_list[index], element)
        if sublist_index != -1:
            return index
        
    return find_first_occurrence(my_list, element, index + 1)