"""
QUESTION:
Write a function named `sort_tuples` that sorts a list of tuples in ascending order. Each tuple contains two elements: a string and an integer. The tuples should be sorted first by the string and then by the integer. The function should not use any built-in sort methods or the `sorted()` function, and it should not rely on any external libraries.
"""

def sort_tuples(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j][0] > lst[j+1][0]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif lst[j][0] == lst[j+1][0]:
                if lst[j][1] > lst[j+1][1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst