"""
QUESTION:
Create a function named `multiply_number` that takes two arguments: `number` (an integer greater than zero) and `integer_list` (a list of at least one positive integer). The function should return a new list where each element is the corresponding element in `integer_list` multiplied by `number`. The function should also handle invalid inputs, including missing or incorrect data types, values outside the range (0, 10^6], and empty lists, and return an error message in such cases. The time complexity of the solution should be O(n), where n is the length of `integer_list`.
"""

def multiply_number(number, integer_list):
    """
    This function takes a positive integer and a list of positive integers, 
    and returns a new list where each element is the corresponding element 
    in the list multiplied by the given number.

    Args:
        number (int): A positive integer.
        integer_list (list): A list of positive integers.

    Returns:
        list: A new list with each element multiplied by the given number.
        str: An error message if the input is invalid.
    """

    # Check if number is not provided or is of wrong data type
    if number is None or not isinstance(number, int):
        return "Number is missing or not an integer."
    
    # Check if number is greater than zero
    if number <= 0:
        return "Number must be greater than zero."
    
    # Check if integer_list is not provided or is of wrong data type
    if integer_list is None or not isinstance(integer_list, list):
        return "List is missing or not a list of positive integers."
    
    # Check if integer_list is empty
    if len(integer_list) == 0:
        return "List must contain at least one element."
    
    # Check if number or any element in the list exceeds 10^6
    if number > 10**6 or any(element > 10**6 for element in integer_list):
        return "Number or elements in the list exceed the maximum value of 10^6."
    
    # Multiply each element in the list by the number
    multiplied_list = [element * number for element in integer_list]
    
    return multiplied_list