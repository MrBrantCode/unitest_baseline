"""
QUESTION:
Write a recursive function named `recursive_sort` that sorts a given list of integers in descending order. The function should take a list of integers as input and return the sorted list without using any built-in sorting functions. The function should be able to handle lists of any length, including empty lists and lists with a single element.
"""

def recursive_sort(input_list):
    # If list is of one element or empty, return the list
    if len(input_list) <= 1:
        return input_list

    # else find max element and its index.
    max_el = max(input_list)
    max_index = input_list.index(max_el)

    # Swap first element and max element
    input_list[0], input_list[max_index] = input_list[max_index], input_list[0]
    
    # Get the sorted list for rest of the list 
    rest_sorted = recursive_sort(input_list[1:])
    
    # return list with first element and then rest of the sorted elements
    return [input_list[0]] + rest_sorted