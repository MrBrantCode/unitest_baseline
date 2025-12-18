"""
QUESTION:
Write a function `get_unique_elements` that takes a list as input and returns a new list containing only the unique elements from the input list. The function should not use any built-in functions or libraries, and it should have a time complexity of O(n^2), where n is the length of the input list. The input list may contain elements of different data types. If the input list is empty, the function should return an empty list.
"""

def get_unique_elements(lst):
    unique_lst = []
    for i in range(len(lst)):
        is_unique = True
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            unique_lst.append(lst[i])
    return unique_lst