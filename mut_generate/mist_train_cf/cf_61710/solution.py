"""
QUESTION:
Implement the function `is_conditions_met(y)` that takes a variable `y` as input and a list of conditions. The function should return `True` if all conditions are met, otherwise it should return a string specifying the first condition that was not met. The conditions are: the variable should be an integer, the variable should be even, and the variable should be greater than or equal to 40.
"""

def is_conditions_met(y):
    conditions = [
        ("Wrong type", lambda y: isinstance(y, int)),
        ("Not even", lambda y: y % 2 == 0),
        ("Less than 40", lambda y: y >= 40)
    ]
    
    for error_message, condition in conditions:
        if not condition(y):
            return error_message
    
    return True