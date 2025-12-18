"""
QUESTION:
Implement a Python function `process_data` that takes the following parameters: 
- `phases`: A list of strings representing different phases.
- `case`: An object providing data retrieval functionality.
- `x_var`: A string representing a variable name.
- `x_unit`: A string representing the units for the variable.
- `figsize`: A tuple representing the figure size, defaulting to `(8.5, 11)` if not provided.

The function should iterate through each phase, retrieve the variable values using the `case.get_val` method, concatenate these values into a single NumPy array, and append it to a list. It should also determine the file counter and counter within the file based on certain conditions. The function should return the list of concatenated arrays, the file counter, and the counter within the file.
"""

import numpy as np

def process_data(phases, case, x_var, x_unit, figsize=(8.5, 11)):
    """
    This function processes data by retrieving variable values for different phases and 
    concatenating them into a single NumPy array.

    Parameters:
    phases (list): A list of strings representing different phases.
    case (object): An object providing data retrieval functionality.
    x_var (str): A string representing a variable name.
    x_unit (str): A string representing the units for the variable.
    figsize (tuple, optional): A tuple representing the figure size. Defaults to (8.5, 11).

    Returns:
    tuple: A tuple containing a list of concatenated arrays, the file counter, and the counter within the file.
    """

    val_list = []
    for phase in phases:
        val_list.append(case.get_val(phase + '.' + x_var, units=x_unit))
    x_vec = np.concatenate(val_list)
    
    file_counter = -1
    counter_within_file = 0

    return [x_vec], file_counter, counter_within_file