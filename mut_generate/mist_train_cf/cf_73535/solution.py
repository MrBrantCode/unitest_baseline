"""
QUESTION:
Develop a function `find_5tuple(y)` that takes an integer `y` and returns the smallest Pythagorean quintuplet (a, b, c, d, e) where a ≤ b ≤ c ≤ d ≤ e and a^2 + b^2 + c^2 + d^2 = e^2 with a sum equal to `y`. The function should return the quintuplet in sorted ascending order. If no such quintuplet exists, return "No possible quintuplet exists for this integer." The input `y` should be in the range 50 to 100.
"""

def entrance(y):
    if y < 50 or y > 100:
        return "Integer y should be in range between 50 and 100."

    for a in range(1, y):
        for b in range(a, y):
            for c in range(b, y):
                for d in range(c, y):
                    e = y - a - b - c - d
                    if e > d and a**2 + b**2 + c**2 + d**2 == e**2:
                        return [a, b, c, d, e]

    return "No possible quintuplet exists for this integer."