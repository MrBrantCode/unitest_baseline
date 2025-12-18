"""
QUESTION:
Create a Python function named `remove_duplicates` to remove duplicate elements from a given list while maintaining the original order of elements. The function should return the updated list. It must have a time complexity of O(n^2), not use any built-in functions or methods that directly remove duplicates, and only use basic list operations. It should handle lists with up to 1,000,000 elements, containing integers, floats, and strings, and remove duplicates case-insensitively for strings.
"""

def remove_duplicates(lst):
    if len(lst) < 2:
        return lst

    result = [lst[0]]
    for i in range(1, len(lst)):
        is_duplicate = False
        for j in range(i):
            if type(lst[i]) != type(lst[j]):
                continue
            if isinstance(lst[i], str) and lst[i].lower() == lst[j].lower():
                is_duplicate = True
                break
            if lst[i] == lst[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            result.append(lst[i])

    return result