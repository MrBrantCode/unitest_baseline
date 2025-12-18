"""
QUESTION:
Write a function `custom_sort` that takes a list containing integers and strings as input, and returns the list sorted in ascending order based on the numeric values of the integers and alphabetical order for the strings. If two elements have the same numeric value or the same alphabetical order, maintain the original order of these elements. The function should handle the case when the input list is empty, have a time complexity of O(n log n), and a space complexity of O(1).
"""

def custom_sort(lst):
    if len(lst) == 0:
        return lst
    
    ints = []
    strings = []
    for item in lst:
        if isinstance(item, int):
            ints.append(item)
        elif isinstance(item, str):
            strings.append(item)
    
    ints.sort()
    strings.sort()
    
    result = []
    i = 0
    j = 0
    for item in lst:
        if isinstance(item, int):
            result.append(ints[i])
            i += 1
        elif isinstance(item, str):
            result.append(strings[j])
            j += 1
    
    return result