"""
QUESTION:
Implement a function called `common_elements` that takes two lists `lst1` and `lst2` as input and returns a new list containing only the elements that are present in both input lists. The implementation should not use any built-in Python functions or libraries.
"""

def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        for j in lst2:
            if i == j and i not in common:
                common.append(i)
                break
    return common