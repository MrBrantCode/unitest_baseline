"""
QUESTION:
Create a function named `unique_elements` that takes a list as a parameter and returns a new list containing only the unique elements from the original list. The solution must not use any built-in functions or libraries. The time complexity of the solution should be O(n^2), where n is the length of the input list.
"""

def unique_elements(lst):
    unique_lst = []
    for i in range(len(lst)):
        is_unique = True
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            unique_lst.append(lst[i])
    return unique_lst