"""
QUESTION:
Create a function named `solve_quadratic(a, b, c)` that calculates the roots of a quadratic equation in the form of ax² + bx + c = 0, where 'a', 'b', and 'c' are real numbers. The function should be able to handle cases where 'a' equals 0 (resulting in a linear equation) and when the discriminant (b² - 4ac) is negative (resulting in complex roots).
"""

import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        if b != 0:
            # The equation becomes a linear equation bx + c = 0 --> x = -c/b
            return -c / b
        else:
            if c == 0:
                # This isn't meaningful as it stands for 0 = 0
                return "This is an identity."
            else:
                # This stands for the absurd equation 0c = 0, with !c
                return "This is a contradiction."
    else:
        # Calculate the discriminant
        d = (b**2) - (4*a*c)

        # Two solutions
        root1 = (-b-cmath.sqrt(d))/(2*a)
        root2 = (-b+cmath.sqrt(d))/(2*a)

        if d < 0:
            return "The equation has two complex roots: {} and {}".format(root1, root2)
        elif d == 0:
            return "The equation has one real root: {}".format(root1)
        else:
            return "The equation has two real roots: {} and {}".format(root1, root2)