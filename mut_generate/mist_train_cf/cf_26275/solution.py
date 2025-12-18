"""
QUESTION:
Create a function called `quadratic_equation(a, b, c)` that calculates the roots of a quadratic equation of the form `ax^2 + bx + c = 0`. The function should return the solutions for the equation. If the equation has no real solutions, it should return "No real solutions". If the equation has one real solution, it should return that solution. If the equation has two real solutions, it should return both solutions as a pair.
"""

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        return ((-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a))