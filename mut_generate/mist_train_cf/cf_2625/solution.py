"""
QUESTION:
Design a function `multiply_list_elements` that takes a list of unique numbers (up to 1000 elements, including integers and floats) and a number as input, and returns a new list where all elements are multiplied by the absolute value of the given number. If the input number is zero, return an empty list.
"""

def multiply_list_elements(lst, num):
    if num == 0:
        return []
    
    return [abs(element) * abs(num) for element in lst]