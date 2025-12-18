"""
QUESTION:
Write a function `run_truncated_prism_volume` that calculates the volume of a truncated prism given the side lengths of the two triangles that form the prism and the height of the prism. The function should return the volume of the prism, rounded to two decimal places, or "Invalid parameters" if the input parameters do not form valid triangles or the height is not positive. The volume of the prism can be calculated using the formula `1/3 * h * (A1 + A2 + √(A1 * A2))`, where `A1` and `A2` are the areas of the two triangles.
"""

def run_truncated_prism_volume(a1, b1, c1, a2, b2, c2, h):
    def check_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def triangle_area(a, b, c):
        sp = (a + b + c) / 2.0 
        return (sp * (sp - a) * (sp - b) * (sp - c)) ** 0.5 

    if h <= 0 or not all(check_valid_triangle(*triangle) for triangle in [(a1, b1, c1), (a2, b2, c2)]):
        return "Invalid parameters"

    else:
        A1 = triangle_area(a1, b1, c1)
        A2 = triangle_area(a2, b2, c2)

        volume = (h * (A1 + A2 + (A1 * A2) ** 0.5)) / 3.0
        return round(volume, 2)