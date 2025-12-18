"""
QUESTION:
Compute the surface area of multiple isosceles triangles with non-uniform sides. Create a function `compute_area` that takes a list of triangle dimensions as input, where each item is a dictionary with keys: 'Side1', 'Side2', 'Base' (all integer values), and returns a list of surface areas for valid isosceles triangles and error messages for invalid dimensions. 

The function should check if the sum of the lengths of the two sides is greater than the length of the base and if the triangle is isosceles (i.e., 'Side1' == 'Side2'). If the dimensions are valid, calculate the surface area using Heron's formula; otherwise, return an error message. Round the surface area to 2 decimal places. The function signature should be `def compute_area(triangles: List[Dict[str, int]]) -> Union[List[float], str]:`
"""

import math
from typing import List, Dict, Union

def compute_area(triangles: List[Dict[str, int]]) -> Union[List[float], str]:
    area_res = []
    for triangle in triangles:
        side1 , side2, base = triangle['Side1'], triangle['Side2'], triangle['Base'] 

        if (side1 + side2) > base and side1 == side2:  
            semi_perimeter = (2 * side1 + base) / 2  # Calculation of semi-perimeter
            area = (semi_perimeter*(semi_perimeter-base)*(semi_perimeter-side1)*(semi_perimeter-side1))**0.5
            area_res.append(round(area,2))
            
        else:
            area_res.append("Invalid dimensions for triangle")
    return area_res