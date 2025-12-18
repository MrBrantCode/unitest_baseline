"""
QUESTION:
Design a function `multiply_list` that takes two parameters: a list of unique integers and floats (maximum length 1000) and a number. The function should return a list where all elements are multiplied by the absolute value of the given number. If the input number is zero, the function should return an empty list.
"""

def multiply_list(input_list, input_number):
    """
    This function takes a list of unique integers and floats and a number, 
    then returns a list where all elements are multiplied by the absolute value of the given number.
    
    If the input number is zero, the function returns an empty list.

    Parameters:
    input_list (list): A list of unique integers and floats.
    input_number (int or float): A number to multiply the list elements with.

    Returns:
    list: A list of elements multiplied by the absolute value of the input number.
    """
    if input_number == 0:
        return []
    
    return [abs(element) * abs(input_number) for element in input_list]