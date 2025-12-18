"""
QUESTION:
Create a function named `is_right_triangle` that takes three parameters `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. The function should return `True` if the triangle is a right-angled triangle and `False` otherwise, using the Pythagorean theorem. The function must handle invalid side lengths, such as negative values or combinations that do not form a valid triangle. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def is_right_triangle(a, b, c):
    # Check for negative side lengths or side lengths that are not valid for a triangle
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or b + c <= a or c + a <= b:
        return False
    
    # Use the Pythagorean theorem to check if the triangle is right-angled
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    
    return False