"""
QUESTION:
Implement the `external_variable` function to take a list of variables and an index, and return a value based on the index and the values in the list. The function should return the sum of the values at indices 1 and 2 for index 0, the product of the values at indices 0 and 3 for index 1, the sum of all values except the one at the given index for index 2, and the product of the values at indices 0, 1, and 2 for index 3.

Implement the `compute_computed_constants` function to calculate and return computed constants based on the given variables. The function should take a list of variables as input and return a list of computed constants. The function signature is `def compute_computed_constants(variables):`.
"""

def entance(variables, index):
    if index == 0:
        return variables[1] + variables[2]
    elif index == 1:
        return variables[0] * variables[3]
    elif index == 2:
        return variables[0] + variables[1] + variables[3]
    elif index == 3:
        return variables[0] * variables[1] * variables[2]

def compute_computed_constants(variables):
    computed_constants = []
    for var in variables:
        computed_constants.append(var * 2)  # Example computation, replace with actual computation
    return computed_constants