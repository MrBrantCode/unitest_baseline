"""
QUESTION:
Write a function called `quad_eqn(a, b, c)` that takes the coefficients of a quadratic equation `ax² + bx + c = 0` as input and returns the roots of the equation. The function should use the quadratic formula and be able to handle complex roots. Test the function with at least five different quadratic equations.
"""

import cmath

def quad_eqn(a, b, c):
  # calculating the discriminant
  dis = (b**2) - (4*a*c)

  # calculating the two solutions
  sol1 = (-b - cmath.sqrt(dis))/(2*a)
  sol2 = (-b + cmath.sqrt(dis))/(2*a)

  return sol1, sol2