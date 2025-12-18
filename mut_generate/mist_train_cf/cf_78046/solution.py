"""
QUESTION:
Write a function called `triangle_properties(a, b, c)` that takes three side lengths of a triangle as input and returns a dictionary containing various geometric properties of the triangle, including:

*   Type of triangle (Equilateral, Isosceles, Scalene)
*   Semiperimeter
*   Perimeter
*   Area (using Heron's formula)
*   Circumradius (for Equilateral triangles)
*   Inradius (for Right-angled triangles)
*   Whether the triangle is Right-angled or not

The function should first check if the given side lengths form a valid triangle. If not, it should return an error message. The function should handle precision issues when checking for Right-angled triangles.
"""

import math

def triangle_properties(a, b, c):
    properties = {} 
    #Checking if triangle is valid
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return "Not a valid triangle"
    #Calculating Semiperimeter
    s = (a + b + c) / 2
    #Calculating Area using Heron's Formula
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    properties['Semiperimeter'] = s
    properties['Area'] = area
    #Calculating Perimeter
    properties['Perimeter'] = 2 * s
    
    #Checking if triangle is equilateral, isosceles or scalene
    if a==b==c:
        properties['Type'] = 'Equilateral'
        properties['Circumradius'] = a / math.sqrt(3)
    elif a==b or b==c or c==a:
        properties['Type'] = 'Isosceles'
    else :
        properties['Type'] = 'Scalene'
        
    #Checking if triangle is right angled 
    sides = [a, b, c]
    sides.sort()
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        properties['Right angled'] = 'Yes'
        properties['Inradius'] = area / s
    else :
        properties['Right angled'] = 'No'
     
    return properties