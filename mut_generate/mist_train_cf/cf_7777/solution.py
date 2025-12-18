"""
QUESTION:
Create a function `manipulate_list` that takes a list of positive integers between 1 and 100 as input, doubles each element using list comprehension, and returns the resulting list in ascending order without modifying the original list. The function should handle duplicate elements and an empty list efficiently, and implement its own sorting algorithm without using built-in sorting functions or libraries.
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