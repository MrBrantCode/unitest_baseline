"""
QUESTION:
Write a function `remove_elements(lst, element)` that takes a list `lst` and an `element` as input, and returns a new list with all occurrences of `element` removed while maintaining the original order of the remaining elements. The function should have a time complexity of O(n) and should not use any built-in functions or libraries to remove the elements.
"""

def remove_elements(lst, element):
    result = []
    for num in lst:
        if num != element:
            result.append(num)
    return result