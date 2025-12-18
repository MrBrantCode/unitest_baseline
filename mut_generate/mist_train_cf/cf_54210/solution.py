"""
QUESTION:
Write a function `consolidate_elements(lst)` that takes a list `lst` as input and returns a new list where successive identical elements in `lst` are consolidated into distinct subarrays. The function should return an empty list if `lst` is empty.
"""

def consolidate_elements(lst):
    if not lst:
        return []

    result = [[lst[0]]]
    for element in lst[1:]:
        if element == result[-1][0]:
            result[-1].append(element)
        else:
            result.append([element])
            
    return result