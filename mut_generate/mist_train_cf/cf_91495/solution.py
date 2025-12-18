"""
QUESTION:
Design a function called `multiply_list_elements` that takes a list of integers and floats and a number as input, and returns a new list where all elements are multiplied by the absolute value of the given number. The input list is limited to a maximum of 1000 elements.
"""

def multiply_list_elements(input_list, input_number):
    """
    This function takes a list of integers and floats, and a number as input. 
    It returns a new list where all elements are multiplied by the absolute value of the given number.

    Args:
        input_list (list): A list of integers and floats.
        input_number (int/float): A number.

    Returns:
        list: A new list with elements multiplied by the absolute value of the input number.
    """

    multiplied_list = []
    
    for element in input_list:
        if isinstance(element, (int, float)):
            multiplied_element = element * abs(input_number)
            multiplied_list.append(multiplied_element)
    
    return multiplied_list