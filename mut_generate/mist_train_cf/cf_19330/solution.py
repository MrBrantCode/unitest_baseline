"""
QUESTION:
Write a function `determine_triangle_type(a, b, c)` that takes three side lengths of a triangle as input and returns the type of triangle. The function should first check if the triangle is valid by ensuring the sum of any two sides is greater than the third side. If the triangle is valid, it should then check the following conditions in order:

- If all three sides are equal, return "Equilateral Triangle".
- If two sides are equal and the triangle is a right triangle (where the square of the longest side equals the sum of the squares of the other two sides), return "Isosceles and Right-Angled Triangle".
- If two sides are equal and the triangle is not a right triangle, return "Isosceles Triangle".
- If all three sides are different and the triangle is a right triangle, return "Scalene and Right-Angled Triangle".
- If all three sides are different and the triangle is not a right triangle, return "Scalene Triangle".

If the triangle is not valid, return "Invalid Triangle".
"""

def determine_triangle_type(a, b, c):
    if not (a + b > c and b + c > a and c + a > b):
        return "Invalid Triangle"

    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        is_right = True
    else:
        is_right = False

    if a == b == c:
        return "Equilateral Triangle"
    elif a == b and is_right:
        return "Isosceles and Right-Angled Triangle"
    elif a == b:
        return "Isosceles Triangle"
    elif a != b and b != c and c != a and is_right:
        return "Scalene and Right-Angled Triangle"
    elif a != b and b != c and c != a:
        return "Scalene Triangle"