"""
QUESTION:
Implement a function named `solve_equation` that takes an integer `w` as input and returns a list of unique tuples `(x, y, z)` that satisfy the equation `x^4 + y^4 + z^4 = w^4`, where `x`, `y`, `z`, and `w` are positive integers. If no solutions exist, return an empty list.
"""

def solve_equation(w):
    solutions = []
    for x in range(1, w+1):
        for y in range(1, w+1):
            for z in range(1, w+1):
                if x**4 + y**4 + z**4 == w**4:
                    solutions.append((x, y, z))
    return solutions