"""
QUESTION:
Implement a function named `sort_and_remove_duplicates` that takes a list of integers as input, sorts it in descending order without using any built-in sorting functions, and removes any duplicate values. The function should aim to minimize the number of comparisons and swaps performed.
"""

def sort_and_remove_duplicates(unsorted_list):
    sorted_list = []

    while unsorted_list:
        max_value = unsorted_list[0]

        for num in unsorted_list:
            if num > max_value:
                max_value = num

        sorted_list.append(max_value)
        unsorted_list = [num for num in unsorted_list if num != max_value]

    return sorted_list