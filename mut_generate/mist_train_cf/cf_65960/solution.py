"""
QUESTION:
Develop a function called `remove_successive_duplicates` that takes a list as input and returns a tuple containing a new list with successive identical elements removed and the count of removed duplicates. The function should work with lists of varying data types and handle the case where the input list is empty.
"""

def remove_successive_duplicates(lst):
    if not lst:
        return [], 0
    
    new_lst = [lst[0]]
    count = 0
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            new_lst.append(lst[i])
        else:
            count += 1
    
    return new_lst, count