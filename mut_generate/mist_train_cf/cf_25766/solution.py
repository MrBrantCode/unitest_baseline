"""
QUESTION:
Implement a function `bubble_sort` that takes an unsorted list of integers as input and returns the sorted list in ascending order using the bubble sort algorithm. The function should sort the list in-place, meaning it should modify the original list instead of creating a new one.
"""

def bubble_sort(my_list):
    # Do n times
    for i in range(0, len(my_list) - 1):
        # Do n - i - 1 times
        for j in range(0, len(my_list) - 1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list