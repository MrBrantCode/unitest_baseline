"""
QUESTION:
Implement the `sort_list` function, which sorts a given list of integers in ascending order without using any built-in sorting functions or methods. The input list can contain duplicate values. The function should return a new sorted list and leave the original list unchanged.
"""

def sort_list(my_list):
    sorted_list = []
    while my_list:
        smallest = my_list[0]
        for num in my_list:
            if num < smallest:
                smallest = num
        sorted_list.append(smallest)
        my_list.remove(smallest)
    return sorted_list