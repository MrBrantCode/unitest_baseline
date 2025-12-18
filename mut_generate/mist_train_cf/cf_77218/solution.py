"""
QUESTION:
Write a function named `find_pivot` that finds the index of an element in a list of integers where the product of all elements to the left equals the sum of all elements to the right. If no such element is found, return -1.
"""

def find_pivot(lst):
    prod = 1
    s_sum = sum(lst)
    for i in range(len(lst)-1, -1, -1):
        s_sum -= lst[i]
        if prod == s_sum:
            return i
        prod *= lst[i]
    return -1