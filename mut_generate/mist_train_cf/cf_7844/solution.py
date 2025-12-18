"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists as input and returns a list containing all the common elements without any duplicates in descending order. The function should be able to handle lists with up to 100,000 elements and have an efficient time complexity, preferably O(n).
"""

def find_common_elements(list1, list2):
    common_elements = set(list1)
    result = set()
    
    for element in list2:
        if element in common_elements:
            result.add(element)
    
    return sorted(result, reverse=True)