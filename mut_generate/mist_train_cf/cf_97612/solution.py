"""
QUESTION:
Create a function `solve_linear_equations(a, b, c, d, e, f)` that takes in the coefficients a, b, c, d, e, f of a 2x2 system of linear equations in the form:
(ax + by = e)
(cx + dy = f)
The function should return the solutions of the equations in both matrix form and standard form, handling systems of equations with complex coefficients and rounding the solutions to the nearest hundredth for real numbers and the imaginary part.
"""

import numpy as np

def solve_linear_equations(a, b, c, d, e, f):
    # Create the matrix and vector representations of the system of equations
    A = np.array([[a, b], [c, d]])
    B = np.array([e, f])
    # Solve the system of equations
    X = np.linalg.solve(A, B)
    # Return the solutions in both matrix form and standard form
    return A, B, X

def print_solutions(a, b, c, d, e, f, A, B, X):
    # Print the solutions in matrix form
    print("Matrix form:")
    print(f"[({a.real:.2f}+{a.imag:.2f}i) ({b.real:.2f}+{b.imag:.2f}i)] [x] [({e.real:.2f}+{e.imag:.2f}i)]")
    print(f"[({c.real:.2f}+{c.imag:.2f}i) ({d.real:.2f}+{d.imag:.2f}i)] [y] = [({f.real:.2f}+{f.imag:.2f}i)]")
    print()
    # Print the solutions in standard form
    print("Standard form:")
    print(f"x = {X[0].real:.2f}+{X[0].imag:.2f}i")
    print(f"y = {X[1].real:.2f}+{X[1].imag:.2f}i")

# Example usage:
a = complex(3, 2)
b = complex(5, -4)
c = complex(2, -3)
d = complex(4, -7)
e = complex(2, -1)
f = complex(1, 2)

A, B, X = solve_linear_equations(a, b, c, d, e, f)
print_solutions(a, b, c, d, e, f, A, B, X)