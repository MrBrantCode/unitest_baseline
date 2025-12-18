"""
QUESTION:
Create a function called `is_right_angled_triangle` that takes three parameters, representing the lengths of the three sides of the triangle. The function should return True if the triangle is a right-angled triangle and False otherwise. The function should not use the Pythagorean theorem to check if the triangle is right-angled and should handle edge cases such as negative side lengths or side lengths that are not valid for a triangle. The function should have a time complexity of O(n^2), where n is the maximum length among the three sides of the triangle, and a space complexity of O(1).
"""

def is_right_angled_triangle(a, b, c):
    # Check if side lengths are valid for a triangle
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check if triangle inequality holds
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    
    # Check if the square of the longest side is equal to the sum of the squares of the other two sides
    return sides[2]**2 == sides[0]**2 + sides[1]**2