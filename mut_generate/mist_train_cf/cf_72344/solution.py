"""
QUESTION:
Write a function named `find_solutions(z)` that finds all integer solutions (x, y) in the range -50 to 50 for the equation x^3 + y^3 = z, where z is a given integer.
"""

def find_solutions(z):
    solutions = []
    for x in range(-50, 51):
        for y in range(-50, 51):
            if x**3 + y**3 == z:
                solutions.append((x, y))
    return solutions