"""
QUESTION:
Create a function `remove_elements(lst, element)` that removes all occurrences of a given `element` from a list `lst` while maintaining the original order of the remaining elements. The function should have a time complexity of O(n) and not use any built-in functions or libraries to remove the elements.
"""

def remove_elements(lst, element):
    result = []
    for num in lst:
        if num != element:
            result.append(num)
    return result