"""
QUESTION:
Create a function called `sum_of_list` that takes in a list of integers and returns the sum of all the elements in the list. The function should not use any built-in sum() or reduce() functions, loops, or recursion with function calls that exceed the system's maximum recursion depth. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def sum_of_list(lst, index=0):
    if index == len(lst):
        return 0
    else:
        return lst[index] + sum_of_list(lst, index + 1)