"""
QUESTION:
Write a function called `solve_system_of_equations` to generate a solution for a given system of linear equations. The function should take as input the coefficients of the two equations in the form of two lists or tuples of two elements each, where the first element represents the coefficient of x and the second element represents the coefficient of y. For example, the system of equations x + 2y = 10 and 2x + 4y = 20 would be represented as ((1, 2, 10), (2, 4, 20)). The function should return a solution as a string describing the relationship between x and y.
"""

def solve_system_of_equations(equation1, equation2):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Check if the equations are linearly dependent
    if a1 * b2 == a2 * b1:
        # If the equations are linearly dependent, return a string describing the relationship between x and y
        if b1 == 0:
            return f"x = {c1 / a1}"
        else:
            return f"x = {c1 / a1} - {b1 / a1}y"

    # If the equations are not linearly dependent, return a message indicating that
    else:
        return "The system of equations has a unique solution."