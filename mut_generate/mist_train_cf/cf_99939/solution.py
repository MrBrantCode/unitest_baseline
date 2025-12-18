"""
QUESTION:
Write a function named `area_of_trapezoid` that takes four parameters a, b, c, d and returns the area of a trapezoid with parallel sides of length a and b, and non-parallel sides of length c and d, given that the trapezoid's perimeter is 20 units. Assume c > d, and the height of the trapezoid is the absolute difference between c and d divided by 2.
"""

def area_of_trapezoid(a, b, c, d):
    """
    Calculate the area of a trapezoid with parallel sides of length a and b, 
    and non-parallel sides of length c and d.

    Parameters:
    a (float): length of the first parallel side
    b (float): length of the second parallel side
    c (float): length of the first non-parallel side
    d (float): length of the second non-parallel side

    Returns:
    float: area of the trapezoid
    """
    h = abs(c - d) / 2
    return (h * (a + b)) / 2