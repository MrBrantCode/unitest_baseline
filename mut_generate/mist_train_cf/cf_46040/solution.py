"""
QUESTION:
Create a function named `multiply_tuple_elements` that takes two parameters: a tuple of numbers and a list. The function should multiply all the numbers in the tuple, append the result to the list, and return the updated list. If the tuple is empty, the function should return an error message instead. The function should work correctly for tuples containing zero, negative numbers, and positive numbers.
"""

def multiply_tuple_elements(my_tuple, my_list):
    if not my_tuple:
        return "Error: Tuple is empty!"
    
    result = 1
    for num in my_tuple:
        result *= num
    my_list.append(result)
    return my_list