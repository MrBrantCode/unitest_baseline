"""
QUESTION:
Write a function `manipulate_list` that takes a list of positive integers as input, doubles each element, sorts the resulting list in ascending order without using any built-in sorting functions or libraries, and returns the sorted list without modifying the original list. The function should handle duplicate elements, empty lists, and lists with elements between 1 and 100 efficiently.
"""

def manipulate_list(lst):
    # Create a new list by doubling every element in the original list
    doubled_lst = [2*x for x in lst]

    # Sort the new list using bubble sort algorithm
    n = len(doubled_lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if doubled_lst[j] > doubled_lst[j+1]:
                doubled_lst[j], doubled_lst[j+1] = doubled_lst[j+1], doubled_lst[j]

    return doubled_lst