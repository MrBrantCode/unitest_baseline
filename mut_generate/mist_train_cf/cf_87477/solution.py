"""
QUESTION:
Create a function `alternate_concatenate(list1, list2)` that concatenates two lists in alternating order without using the "+" operator or the "extend" method. The function should use recursion. If one of the input lists is empty, the function should return the other list.
"""

def alternate_concatenate(list1, list2):
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        return [list1[0]] + [list2[0]] + alternate_concatenate(list1[1:], list2[1:])