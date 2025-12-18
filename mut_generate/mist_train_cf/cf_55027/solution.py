"""
QUESTION:
Write a function `advanced_triangle_solver` that takes 9 positive integer arguments representing the side lengths of three triangles. For each triangle, classify it as 'void', 'scalene', 'isosceles', or 'equilateral' based on the triangle formation conditions, and calculate its area using Heron's formula with a precision to 2 decimal places. Return a tuple containing a list of triangle types and a list of corresponding areas. If any input is invalid (i.e., non-positive or does not meet the triangle formation conditions), return -1.
"""

def advanced_triangle_solver(a, b, c, d, e, f, g, h, i):
    def calculate_area(x, y, z):
        s = (x + y + z)/2
        return round((s*(s-x)*(s-y)*(s-z)) ** 0.5, 2)

    def classify_triangle(x, y, z):
        if x + y > z and x + z > y and y + z > x:
            if x == y == z:
                return 'Equilateral'
            elif x == y or y == z or z == x:
                return 'Isosceles'
            else:
                return 'Scalene'
        else:
            return 'void'

    triangles = [(a, b, c), (d, e, f), (g, h, i)]
    types = []
    areas = []

    for triangle in triangles:
        x, y, z = triangle
        if min(triangle) <= 0:
            return -1

        type_of_triangle = classify_triangle(x, y, z)
        types.append(type_of_triangle)
        if type_of_triangle != 'void':
            areas.append(calculate_area(x, y, z))
        else:
            areas.append(-1)

    return types, areas