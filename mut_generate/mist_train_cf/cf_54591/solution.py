"""
QUESTION:
Define the function sum_triangle_areas(r_max) to compute the sum of the smallest non-degenerate spherical triangle areas for a sphere with radius r ranging from 1 to r_max. The area of the smallest spherical triangle for a given radius r is 0.05 * r^2 for r > 1, and 0 for r = 1. The function should return the sum rounded to six decimal places.
"""

def sum_triangle_areas(r_max):
    """
    Compute the sum of the smallest non-degenerate spherical triangle areas 
    for a sphere with radius r ranging from 1 to r_max.
    
    Args:
    r_max (int): The maximum radius of the sphere.
    
    Returns:
    float: The sum of the smallest non-degenerate spherical triangle areas 
           rounded to six decimal places.
    """
    return round(sum(0.05 * r**2 for r in range(2, r_max + 1)), 6)