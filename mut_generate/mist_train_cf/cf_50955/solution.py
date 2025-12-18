"""
QUESTION:
Given a constraint that involves a product of variables, determine if it's possible to represent this constraint in a linear form for the purpose of linear optimization. If not, are there any special conditions under which the constraint can be linearized, such as one variable being binary or both variables being integers with small upper bounds?
"""

def linearize_constraint(x, y):
    """
    This function determines if a constraint involving a product of variables can be linearized.
    
    Parameters:
    x (int): The first variable in the constraint.
    y (int): The second variable in the constraint.
    
    Returns:
    str: A message indicating whether the constraint can be linearized and under what conditions.
    """
    if x == 0 or y == 0:
        return "The constraint is already linear."
    elif x == 1 or y == 1:
        return "The constraint can be linearized if one variable is binary (0 or 1)."
    elif x < 2 and y < 2:
        return "The constraint can be linearized if both variables are integers with small upper bounds."
    else:
        return "The constraint cannot be linearized."