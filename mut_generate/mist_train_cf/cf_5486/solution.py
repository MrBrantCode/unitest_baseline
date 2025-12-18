"""
QUESTION:
Write a function `get_unique_elements` that takes a list as input and returns the number of unique elements in the list. The function must have a time complexity of O(n^2) and cannot use any additional data structures or built-in functions for finding unique elements.
"""

def get_unique_elements(lst):
    unique_count = 0
    n = len(lst)
    
    for i in range(n):
        is_unique = True
        for j in range(i+1, n):
            if lst[i] == lst[j]:
                is_unique = False
                break
        
        if is_unique:
            unique_count += 1
    
    return unique_count