"""
QUESTION:
Write a function `linear_search` that takes a list `lst` and an `element` as input, and returns a list of indices where the `element` appears in `lst`. The function should be able to handle lists with duplicate elements.
"""

def linear_search(lst, element):
    indices = []
    for i in range(len(lst)):
        if lst[i] == element:
            indices.append(i)
    return indices