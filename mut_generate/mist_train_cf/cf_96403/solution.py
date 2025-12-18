"""
QUESTION:
Write a recursive function `operate` that takes a list of integers `lst` and returns a modified list. The function should follow these rules: 
- If `lst` contains only one element, return `lst` as it is.
- If `lst` contains two elements, return a new list with the sum of the two elements.
- If `lst` contains more than two elements, return a new list with the first element replaced by the sum of the first two elements, and the rest of `lst` remains unchanged. 
The function should raise an exception if `lst` is empty or contains any element that is not an integer.
"""

def operate(lst):
    if len(lst) == 0:
        raise Exception("List is empty")
    if not all(isinstance(x, int) for x in lst):
        raise Exception("List contains non-integer element")

    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return [lst[0] + lst[1]]
    else:
        return [lst[0] + lst[1]] + lst[2:]