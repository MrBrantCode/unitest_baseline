"""
QUESTION:
Write a function called `remove_item(lst, item)` that removes all occurrences of `item` from list `lst` while maintaining the relative order of the remaining items. The function must have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1), meaning no additional data structures can be used. The function should modify the input list in-place and return the modified list.
"""

def remove_item(lst, item):
    i = 0
    j = 0
    
    while i < len(lst):
        if lst[i] == item:
            i += 1
        else:
            lst[j] = lst[i]
            i += 1
            j += 1
    
    del lst[j:]
    return lst