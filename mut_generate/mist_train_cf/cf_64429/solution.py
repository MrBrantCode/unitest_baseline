"""
QUESTION:
Create a function `calculate_volumetric_value` that takes the coordinates (x, y, z) of four points in 3D space as input and returns the volume of the tetrahedron formed by these points. The function should calculate the volume using the determinant formula and return the absolute value divided by 6.
"""

def calculate_volumetric_value(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    volume = abs((x1*(y2*(z3-z4) + y3*(z4-z2) + y4*(z2-z3)) - x2*(y1*(z3-z4) + y3*(z4-z1) + y4*(z1-z3)) 
                  + x3*(y1*(z2-z4) + y2*(z4-z1) + y4*(z1-z2)) - x4*(y1*(z2-z3) + y2*(z3-z1) + y3*(z1-z2)))/6)
    return volume