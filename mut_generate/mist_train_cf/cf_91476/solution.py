"""
QUESTION:
Write a function called `reverse_list` that takes a list as input and returns the reversed list without using the `reverse()` method or any built-in Python functions or methods. The function should iterate over the indices of the input list in reverse order and construct the reversed list from the elements at those indices.
"""

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst