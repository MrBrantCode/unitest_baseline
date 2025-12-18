"""
QUESTION:
Given expressions I. f(w,w), II. f(x,1), and III. f(y,g(z)), determine which pairs of expressions can be considered unifiable, with the restriction that only variables w, x, y, and z are present, and a function g is defined. Write a function named `check_unifiable` that takes two expressions as input and returns a boolean indicating whether the two expressions can be unifiable.
"""

def check_unifiable(expr1, expr2):
    """
    Check if two expressions are unifiable.

    Args:
    expr1 (tuple): The first expression.
    expr2 (tuple): The second expression.

    Returns:
    bool: True if the expressions are unifiable, False otherwise.
    """

    # Base case: if both expressions are the same, they are unifiable
    if expr1 == expr2:
        return True

    # If one expression is a variable and the other is a function, they are not unifiable
    if (isinstance(expr1, str) and isinstance(expr2, tuple)) or (isinstance(expr2, str) and isinstance(expr1, tuple)):
        return False

    # If both expressions are variables, they are unifiable
    if isinstance(expr1, str) and isinstance(expr2, str):
        return True

    # If both expressions are functions, check their arguments
    if isinstance(expr1, tuple) and isinstance(expr2, tuple):
        # If the functions have different names, they are not unifiable
        if expr1[0] != expr2[0]:
            return False

        # If the functions have different numbers of arguments, they are not unifiable
        if len(expr1) != len(expr2):
            return False

        # Check the arguments of the functions
        for arg1, arg2 in zip(expr1[1:], expr2[1:]):
            # If the arguments are not unifiable, the expressions are not unifiable
            if not check_unifiable(arg1, arg2):
                return False

        # If all arguments are unifiable, the expressions are unifiable
        return True

    # If none of the above conditions are met, the expressions are not unifiable
    return False