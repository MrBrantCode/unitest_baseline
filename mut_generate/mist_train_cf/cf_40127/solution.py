"""
QUESTION:
Implement a function `calculate_sum_of_multiples(variables, multiple)` that takes a dictionary `variables` where keys are variable names and values are corresponding numerical values, and an integer `multiple`. The function should return the sum of the values for the variables that are multiples of the given number. The variable name is in the format 'varX' where X is an integer.
"""

def entrance(variables, multiple):
    sum_of_multiples = 0
    for var_name, value in variables.items():
        if int(var_name[3:]) % multiple == 0:  # Extract the number from the variable name and check if it's a multiple
            sum_of_multiples += value
    return sum_of_multiples