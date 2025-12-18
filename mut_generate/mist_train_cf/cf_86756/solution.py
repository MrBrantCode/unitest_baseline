"""
QUESTION:
Write a function called `find_common_elements` that takes two lists as parameters and returns a new list containing the elements that are common to both lists. The function should not use any built-in functions or libraries that directly solve the problem and should have a time complexity of O(n^2), where n is the length of the longer list. The function should handle edge cases such as empty lists or lists with duplicate elements.
"""

def find_common_elements(list1, list2):
    common_elements = []
    longer_list = list1 if len(list1) >= len(list2) else list2
    shorter_list = list1 if len(list1) < len(list2) else list2
    
    for element in shorter_list:
        if element in longer_list and element not in common_elements:
            common_elements.append(element)
    
    return common_elements