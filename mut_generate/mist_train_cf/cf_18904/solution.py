"""
QUESTION:
Write a function `common_elements` that takes two lists as input and returns a list of common elements between them, without using built-in functions like `set()` or `intersection()`, loops, or conditional statements.
"""

def common_elements(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
            
    return result