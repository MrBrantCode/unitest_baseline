"""
QUESTION:
Write a function `remove_duplicates_reverse` that takes a list of integers as input, removes duplicate elements keeping only the first occurrence of each element, and returns the modified list in reverse order. The function should use a single loop and no additional data structures other than the input and output lists. The solution should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates_reverse(lst):
    seen = set()
    result = []
    
    for i in range(len(lst)-1, -1, -1):
        if lst[i] not in seen:
            seen.add(lst[i])
            result.append(lst[i])
    
    return result