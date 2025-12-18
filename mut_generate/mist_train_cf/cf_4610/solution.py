"""
QUESTION:
Create a function named `is_right_angled_triangle` that takes three parameters representing the lengths of the three sides of a triangle. The function should return True if the triangle is a right-angled triangle and False otherwise. The function should not use the Pythagorean theorem to check if the triangle is right-angled and should handle edge cases such as negative side lengths or side lengths that are not valid for a triangle. The time complexity of the function should be O(n^2) and the space complexity should be O(1), where n is the maximum length among the three sides of the triangle.
"""

def is_right_angled_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    sides = sorted([a, b, c])
    
    return sides[2]**2 == sides[0]**2 + sides[1]**2