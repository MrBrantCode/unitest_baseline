"""
QUESTION:
Write a function `check_triangle_type(a, b, c)` that takes the lengths of the three sides of a triangle as input and returns a string representing the type of the triangle. The function should classify the triangle as "Equilateral" if all sides are equal, "Isoceles" if any two sides are equal, and "Scalene" if no sides are equal. If the provided lengths cannot form a valid triangle (i.e., if any side is longer than the sum of the other two), the function should return "These lengths cannot form a valid triangle".
"""

def check_triangle_type(a, b, c):
    # checks if a valid triangle can be formed
    if a + b <= c or a + c <= b or b + c <= a:
        return "These lengths cannot form a valid triangle"
    # if all sides are equal
    elif a == b == c:
        return "Equilateral"
    # if any two sides are equal
    elif a == b or b == c or c == a:
        return "Isoceles"
    # if no sides are equal
    else:
        return "Scalene"