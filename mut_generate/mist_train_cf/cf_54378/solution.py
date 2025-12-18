"""
QUESTION:
Create a function named `find_roots` that takes three parameters: `a`, `b`, and `c`, representing the coefficients of a quadratic equation ax² + bx + c = 0, where a ≠ 0.

Using the quadratic formula x = [-b ± sqrt(b² - 4ac)] / (2a), calculate the roots of the equation and return their values along with a message indicating their nature. The function should handle all four possible discriminant values: > 0, = 0, < 0, and undefined/NaN, corresponding to two distinct real roots, two identical real roots, two complex roots, and no real solution, respectively.

Restrictions:

- 'a' must not be zero.
- The function should handle division by zero.
- The function should use the cmath library for handling complex roots.
- The function should print the calculated roots and the corresponding message.
"""

import cmath

def find_roots(a, b, c):
    if a == 0:
        print("Invalid input, a cannot be 0")
        return
    
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f'The equation has two distinct real roots: {root1} and {root2}')
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)
        print(f'The equation has two identical real roots: {root1}')
    elif discriminant < 0:
        root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2*a)
        print(f'The equation has two complex roots: {root1} and {root2}')
    else:
        print('The discriminant is undefined, so there are no real solutions.')