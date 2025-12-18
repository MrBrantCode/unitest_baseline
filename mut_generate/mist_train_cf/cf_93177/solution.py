"""
QUESTION:
Create a function `remove_duplicates_and_sort` that takes a list as input, removes all non-numeric elements, removes duplicate numbers, and sorts the remaining numbers in descending order. The function should be able to handle large input lists with up to 100,000 elements efficiently.
"""

def remove_duplicates_and_sort(input_list):
    # Remove non-numeric elements
    input_list = [x for x in input_list if isinstance(x, (int, float))]

    # Remove duplicate elements
    input_list = list(set(input_list))

    # Sort the list in descending order
    input_list.sort(reverse=True)

    return input_list