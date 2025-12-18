"""
QUESTION:
Create a function called `reverse_list` that takes a list as input and returns a new list with the elements in reverse order, without using the reverse() method or any built-in Python functions or methods. The input list should remain unchanged.
"""

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst