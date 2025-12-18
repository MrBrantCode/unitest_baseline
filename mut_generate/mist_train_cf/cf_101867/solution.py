"""
QUESTION:
Create a function called `solve_linear_equations` that takes six complex coefficients as input (a, b, c, d, e, f) representing a 2x2 system of linear equations in the form:
(ax + by = e)
(cx + dy = f)

The function should return the solutions of the equations (x and y) in both matrix form and standard form. The solutions should be rounded to the nearest hundredth for real numbers and rounded to the nearest hundredth for the imaginary part.

The input coefficients a, b, c, d, e, f are complex numbers.
"""

import numpy as np

def solve_linear_equations(a, b, c, d, e, f):
    """
    Solve a 2x2 system of linear equations with complex coefficients.

    Parameters:
    a, b, c, d (complex): Coefficients of the linear equations.
    e, f (complex): Constants of the linear equations.

    Returns:
    tuple: Solutions of the equations (x and y) in both matrix form and standard form.
    """

    # Create the matrix and vector representations of the system of equations
    A = np.array([[a, b], [c, d]])
    B = np.array([e, f])

    # Solve the system of equations
    X = np.linalg.solve(A, B)

    # Print the solutions in matrix form
    print("Matrix form:")
    print(f"[({a.real:.2f}+{a.imag:.2f}i) ({b.real:.2f}+{b.imag:.2f}i)] [x] [({e.real:.2f}+{e.imag:.2f}i)]")
    print(f"[({c.real:.2f}+{c.imag:.2f}i) ({d.real:.2f}+{d.imag:.2f}i)] [y] = [({f.real:.2f}+{f.imag:.2f}i)]")
    print()

    # Print the solutions in standard form
    print("Standard form:")
    print(f"x = {X[0].real:.2f}+{X[0].imag:.2f}i")
    print(f"y = {X[1].real:.2f}+{X[1].imag:.2f}i")

    return X