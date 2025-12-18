"""
QUESTION:
Write a function called `get_third_element` that takes a set of integers as a parameter. The function should return the third smallest element in the set without using any built-in sorting functions or converting the set to a list.
"""

def get_third_element(my_set):
    smallest_element = float('inf')
    second_smallest_element = float('inf')
    third_smallest_element = float('inf')
    for element in my_set:
        if element < smallest_element:
            third_smallest_element = second_smallest_element
            second_smallest_element = smallest_element
            smallest_element = element
        elif element < second_smallest_element:
            third_smallest_element = second_smallest_element
            second_smallest_element = element
        elif element < third_smallest_element:
            third_smallest_element = element
    return third_smallest_element