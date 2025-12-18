"""
QUESTION:
Write a function `triangle_type(a, b, c)` that takes the lengths of three sides of a triangle as input and returns the type of the triangle. The function should classify the triangle into one of three types: "EQUILATERAL" (all sides are equal), "ISOSCELES" (two sides are equal), or "SCALENE" (all sides are different).
"""

def triangle_type(a, b, c):
    if a == b == c:
        return "EQUILATERAL"
    elif a == b or a == c or b == c:
        return "ISOSCELES"
    else:
        return "SCALENE"