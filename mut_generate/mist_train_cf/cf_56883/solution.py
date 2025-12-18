"""
QUESTION:
Write a function `get_second_last_element(input_list)` that returns the second-last element of the given list without knowing its length beforehand. The function should return an error message if the list has less than 2 elements.
"""

def get_second_last_element(input_list):
    try:
        return input_list[-2]
    except IndexError:
        return "Error: The length of the list is less than 2"