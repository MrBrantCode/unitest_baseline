"""
QUESTION:
Create a function called `remove_duplicates_and_sort` that takes a list as input. The function should remove all non-numeric elements from the list, eliminate duplicate numbers, sort the remaining numbers in descending order, and return the final list. The function should be able to efficiently handle input lists with up to 100,000 elements.
"""

def remove_duplicates_and_sort(input_list):
    # Remove non-numeric elements
    input_list = [x for x in input_list if isinstance(x, (int, float))]

    # Remove duplicate elements
    input_list = list(set(input_list))

    # Sort the list in descending order
    input_list.sort(reverse=True)

    return input_list