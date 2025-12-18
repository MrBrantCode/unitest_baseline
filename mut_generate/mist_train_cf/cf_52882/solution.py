"""
QUESTION:
Implement a function named `my_sort` that takes a list of integers as input and returns the sorted list in ascending order without using Python's built-in sorting functions. The function should correctly sort the list by comparing and swapping elements.
"""

def my_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list