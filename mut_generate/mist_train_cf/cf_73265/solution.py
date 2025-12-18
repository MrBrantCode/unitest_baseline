"""
QUESTION:
Create a function `triangle_properties` that takes the lengths of the sides of a triangle `a`, `b`, and `c` as input and returns a dictionary containing the properties of the triangle. The properties to be calculated are: semiperimeter, area, perimeter, type (Equilateral, Isosceles, Scalene), whether it is right-angled, and the circumradius (if it is equilateral) and inradius (if it is right-angled). Assume that the input values are valid (i.e., each argument should be a number that can be the length of a side of a triangle).
"""

import math

def triangle_properties(a, b, c):
    properties = {} #dictionary to hold all the properties
    
    #Checking if triangle is valid
    if (a + b <= c) or (a + c <= b) or (b + c <= a): 
        return "Not a valid triangle"
    
    #Calculating Semiperimeter
    s = (a + b + c) / 2
    
    #Calculating Area using Heron's Formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    properties['Semiperimeter'] = s
    properties['Area'] = area
    
    #Calculating Perimeter
    properties['Perimeter'] = a + b + c

    #Checking if triangle is equilateral, isosceles or scalene
    if a==b==c:
        properties['Type'] = 'Equilateral'
        properties['Circumradius'] = a / math.sqrt(3)
    elif a==b or b==c or c==a:
        properties['Type'] = 'Isosceles'
    else:
        properties['Type'] = 'Scalene'
    
    #Checking if triangle is right angled 
    sides = [a, b, c]
    sides.sort()
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        properties['Right angled'] = 'Yes'
        properties['Inradius'] = area / s
    else:
        properties['Right angled'] = 'No'
    
    return properties