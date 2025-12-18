"""
QUESTION:
Write a function called "remove_duplicates_advanced" that takes a list of elements as input and returns a new list with all the duplicate elements removed. Implement this function using only nested loops to compare each element with all the previous elements, without using any built-in Python functions or data structures such as set(), collections.Counter(), dictionaries, or lists.
"""

def remove_duplicates_advanced(lst):
    unique_lst = []
    
    for i in range(len(lst)):
        is_unique = True
        
        for j in range(i):
            if lst[i] == lst[j]:
                is_unique = False
                break
        
        if is_unique:
            unique_lst.append(lst[i])
    
    return unique_lst