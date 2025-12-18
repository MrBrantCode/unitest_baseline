"""
QUESTION:
Write a function called "remove_duplicates_advanced" that takes a list of integers as input and returns a new list with all the duplicate elements removed. Implement the function using only nested loops to traverse the list and compare each element with all the previous elements. Do not use any built-in Python functions or libraries, data structures, or non-primitive data types.
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