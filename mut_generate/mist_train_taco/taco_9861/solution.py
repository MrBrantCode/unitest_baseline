"""
QUESTION:
Write a program which solve a simultaneous equation:

ax + by = c
dx + ey = f

The program should print x and y for given a, b, c, d, e and f (-1,000 ≤ a, b, c, d, e, f ≤ 1,000). You can suppose that given equation has a unique solution.



Input

The input consists of several data sets, 1 line for each data set. In a data set, there will be a, b, c, d, e, f separated by a single space. The input terminates with EOF.

Output

For each data set, print x and y separated by a single space. Print the solution to three places of decimals. Round off the solution to three decimal places.

Examples

Input

1 2 3 4 5 6
2 -1 -2 -1 -1 -5


Output

-1.000 2.000
1.000 4.000


Input

2 -1 -3 1 -1 -3
2 -1 -3 -9 9 27


Output

0.000 3.000
0.000 3.000
"""

def solve_simultaneous_equations(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    """
    Solves the simultaneous equations:
    ax + by = c
    dx + ey = f
    
    Parameters:
    a, b, c, d, e, f (float): Coefficients of the equations.
    
    Returns:
    tuple: A tuple containing the solutions (x, y) rounded to three decimal places.
    """
    # Coefficient matrix A
    A = [a, b, d, e]
    # Constant vector B
    B = [c, f]
    
    # Determinant of matrix A
    detA = A[0] * A[3] - A[1] * A[2]
    
    # Inverse of matrix A
    inA = [A[3], -A[1], -A[2], A[0]]
    
    # Calculate solutions
    solutions = [n / detA for n in [inA[0] * B[0] + inA[1] * B[1], inA[2] * B[0] + inA[3] * B[1]]]
    
    # Round solutions to three decimal places
    x = round(solutions[0], 3)
    y = round(solutions[1], 3)
    
    return (x, y)