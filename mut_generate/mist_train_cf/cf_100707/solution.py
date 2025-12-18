"""
QUESTION:
Write a function `solve_linear_equations(a, b, c, d, e, f)` that takes six complex coefficients as inputs, representing a 2x2 system of linear equations in the form:
(ax + by = e)
(cx + dy = f)
The function should return the solutions of the equations in both matrix and standard forms, with real and imaginary parts rounded to the nearest hundredth.
"""

import numpy as np

def solve_linear_equations(a, b, c, d, e, f):
    # Create the matrix and vector representations of the system of equations
    A = np.array([[a, b], [c, d]])
    B = np.array([e, f])
    # Solve the system of equations
    X = np.linalg.solve(A, B)
    # Return the solutions in both matrix and standard forms
    return {
        "matrix_form": f"[({a.real:.2f}+{a.imag:.2f}i) ({b.real:.2f}+{b.imag:.2f}i)] [x]   [({e.real:.2f}+{e.imag:.2f}i)]\n[({b.real:.2f}-{a.real:.2f}i) ({d.real:.2f}-{c.real:.2f}i)] [y] = [({f.real:.2f}-{e.real:.2f}i)]",
        "standard_form": {
            "x": f"{X[0].real:.2f}+{X[0].imag:.2f}i",
            "y": f"{X[1].real:.2f}+{X[1].imag:.2f}i"
        }
    }