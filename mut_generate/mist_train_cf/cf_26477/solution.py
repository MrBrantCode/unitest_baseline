"""
QUESTION:
Implement a function `stable_uniq` that takes a list as input and returns a new list containing the unique elements in the order they first appeared. The function should maintain the stability of the original order of elements, meaning that if an element appears multiple times in the input list, only the first occurrence should be included in the output list.
"""

def stable_uniq(L):
    seen = set()
    result = []
    for item in L:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result