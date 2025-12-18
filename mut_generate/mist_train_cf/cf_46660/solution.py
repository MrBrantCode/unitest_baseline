"""
QUESTION:
Write a function `multiply(lst)` that takes a non-empty list of integers as input and returns the product of all odd elements located at even indices. The function should also check if any element in the list exceeds 100 and return an error message if it does. If the input list is empty, the function should return an error message.
"""

def multiply(lst):
    # Check if list is empty
    if not lst:
        return "Error: List is empty"
    
    # Check if any value in the list exceeds 100
    for i in lst:
        if i > 100:
            return "Error: List contains values greater than 100"

    return_value = 1  # Initializing the return variable
    for index, value in enumerate(lst):
        # Check if the index is even and the value is odd
        if index % 2 == 0 and value % 2 != 0:
            return_value *= value

    return return_value