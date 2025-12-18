"""
QUESTION:
Write a function named `insertion_sort` that sorts a given list of integers in ascending order using the insertion sort algorithm. The function should take one argument, `unsorted_list`, and return the sorted list. The function should not use any built-in sorting functions or libraries.
"""

def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        current_value = unsorted_list[index]
        position = index

        while position > 0 and unsorted_list[position - 1] > current_value:
            unsorted_list[position] = unsorted_list[position - 1]
            position = position - 1

        unsorted_list[position] = current_value

    return unsorted_list