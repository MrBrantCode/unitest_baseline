"""
QUESTION:
Implement a function named find_common_elements that takes two lists, lst1 and lst2, and returns a new list containing only the elements that appear in both lists, preserving their original order and handling duplicates. The function should achieve this in O(n) time complexity where n is the length of the longest input list, without using built-in Python functions or libraries.
"""

def find_common_elements(lst1, lst2):
    common_elements = []
    elements = {}
    
    # Create a dictionary to store the frequency of elements in lst1
    for i in lst1:
        if i in elements:
            elements[i] += 1
        else:
            elements[i] = 1
    
    # Iterate over lst2 and add elements to common_elements if they exist in elements
    for i in lst2:
        if i in elements and elements[i] > 0:
            common_elements.append(i)
            elements[i] -= 1
    
    return common_elements