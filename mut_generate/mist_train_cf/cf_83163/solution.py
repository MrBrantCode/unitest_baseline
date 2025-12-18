"""
QUESTION:
Write a function `truncated_prism_volume` that calculates and returns the volume of a truncated triangular prism with a precision of 2 decimal points. The function takes seven parameters: the lengths of the three base sides (`a1`, `b1`, `c1`), the lengths of the three top sides (`a2`, `b2`, `c2`), and the height (`h`) of the prism. The function should first validate whether the sides and height represent a valid truncated prism, where a valid prism has the sum of any two sides (both base and top) greater than the third side and a height greater than 0. If the prism is invalid, return "Invalid parameters".
"""

def truncated_prism_volume(a1, b1, c1, a2, b2, c2, h):
    """Calculates and returns the volume of a truncated triangular prism.

    Args:
    a1 (float): The length of the first base side.
    b1 (float): The length of the second base side.
    c1 (float): The length of the third base side.
    a2 (float): The length of the first top side.
    b2 (float): The length of the second top side.
    c2 (float): The length of the third top side.
    h (float): The height of the prism.

    Returns:
    float: The volume of the truncated triangular prism with a precision of 2 decimal points.
    str: "Invalid parameters" if the prism is invalid.
    """

    def check_valid_triangle(a, b, c):
        """Checking if 3 sides can form a valid triangle"""
        return a + b > c and a + c > b and b + c > a 
    
    def triangle_area(a, b, c):
        """Using Heron's Formula to calculate area of a triangle"""
        sp = (a + b + c) / 2.0 # Semi-perimeter
        return (sp*(sp - a)*(sp - b)*(sp - c)) ** 0.5 # √[s(s - a)(s - b)(s - c)]

    if h <= 0 or not all([check_valid_triangle(*triangle) for triangle in [(a1,  b1, c1), (a2, b2, c2)]]):
        return "Invalid parameters"

    else:
        # Area of 2 triangles
        A1 = triangle_area(a1, b1, c1)
        A2 = triangle_area(a2, b2, c2)
        
        # Volume of truncated prism: 1/3 * h * (A1 + A2 + √(A1 * A2)) 
        volume = (h * (A1 + A2 + (A1 * A2) ** 0.5)) / 3.0
        return round(volume, 2)