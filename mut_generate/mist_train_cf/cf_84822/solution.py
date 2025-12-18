"""
QUESTION:
Write a function `find_difference(first_list, second_list)` that takes two lists of floating-point numbers as input and returns the difference between the second smallest number from `first_list` and the second largest number from `second_list`. The function should handle cases where one or both of the lists are empty and can contain duplicate values. If either list has less than two elements, it should return an error message indicating which list needs more elements. If both lists have less than two elements, it should return an error message indicating that both lists need more elements.
"""

def find_difference(first_list, second_list):
    if len(first_list) < 2 and len(second_list) < 2:
        return 'Both lists should have at least two elements'
    elif len(first_list) < 2:
        return 'First list should have at least two elements'
    elif len(second_list) < 2:
        return 'Second list should have at least two elements'
    
    first_list.sort()
    second_list.sort(reverse=True)
    
    second_smallest_in_first_list = first_list[1]
    second_largest_in_second_list = second_list[1]

    return second_smallest_in_first_list - second_largest_in_second_list