"""
QUESTION:
Create a function `remove_duplicates(lst)` that takes a list `lst` as input, where the list can contain integers, floats, strings, or a combination of these data types. The function should return a new list containing the same elements as the input list, but with duplicates removed and the original order maintained. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(lst):
    seen = {}
    result = []
    
    for item in lst:
        if item not in seen:
            seen[item] = True
            result.append(item)
    
    return result