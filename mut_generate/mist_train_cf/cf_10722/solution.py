"""
QUESTION:
Design a function named `multiply_list_elements` that takes a list of up to 1000 integers and floats and a number as parameters. The function should return a new list where all elements from the input list are multiplied by the absolute value of the given number.
"""

def multiply_list_elements(input_list, input_number):
    multiplied_list = []
    
    for element in input_list:
        if isinstance(element, (int, float)):
            multiplied_element = element * abs(input_number)
            multiplied_list.append(multiplied_element)
    
    return multiplied_list