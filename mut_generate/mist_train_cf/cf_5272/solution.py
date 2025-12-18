"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of elements and removes any duplicate elements that are adjacent to each other, while maintaining the order of the elements. The function should return the modified list.

Constraints: 
- The function should have a time complexity of O(n) or less, where n is the length of the input list.
- No additional data structures or new lists can be created.
- The input list may be empty or contain a single element, all elements may be duplicates, and elements may be of different data types.
"""

def remove_duplicates(lst):
    if len(lst) <= 1:
        return lst
    
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i+1]:
            lst.pop(i+1)
        else:
            i += 1
    
    return lst