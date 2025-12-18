"""
QUESTION:
Create a function named `manipulate_variables` that takes two arguments: a variable `b` and a list of integers `num_list`. The function should return the sum of the elements in `num_list` and `b`. However, it must handle potential errors, including: 
- `b` is not a number (int or float)
- `num_list` is not a list
- `num_list` is empty
- `num_list` contains non-integer elements

In case of any error, the function should return a proper error message.
"""

def manipulate_variables(b, num_list):
    # check if variable is a number
    if not (isinstance(b, int) or isinstance(b, float)):
        return "Error: The variable is not a number."

    # check if second argument is a list
    if not isinstance(num_list, list):
        return "Error: Second argument is not a list."
    
    # check if list is empty
    if not num_list:
        return "Error: The list is empty."

    # check if all elements in the list are integers
    if not all(isinstance(num, int) for num in num_list):
        return "Error: The list contains non-integer elements."
    
    # calculate the sum of elements in the list with the given variable
    total_sum = sum(num_list) + b

    return total_sum