"""
QUESTION:
Write a function `multiply_list(my_list)` that takes a list of numbers as input and returns the product of all elements in the list. The function should not use any external libraries or built-in product functions, only basic programming constructs. The input list will contain only integers and will not be empty.
"""

def multiply_list(my_list):
    resultant_value = 1
    for number in my_list:
        resultant_value *= number
    return resultant_value