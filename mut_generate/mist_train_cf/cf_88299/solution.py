"""
QUESTION:
Write a function `remove_duplicates_reverse` that takes a list of integers as input and returns a list containing the unique elements in reverse order, without using any built-in functions, dictionaries, or sets. The function should only keep the first occurrence of each element and must have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates_reverse(lst):
    result = []
    
    for i in range(len(lst)-1, -1, -1):
        if lst[i] not in result:
            result.insert(0, lst[i])
    
    return result