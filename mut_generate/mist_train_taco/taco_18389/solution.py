"""
QUESTION:
Given three sides of a triangle A, B and C in the form of integers. Find the area of the triangle.
Note: The triangle may not exist. In such cases, the area is 0.
Example 1:
Input: A = 2, B = 2, C = 3
Output: 1.984313
Explanation:
The area formed by the triangle whose
sides are 2,2 and 3 units respectively is 
1.984313 units^{2}.
Example 2:
Input: A = 1, B = 3, C = 1
Output: 0.000
Explanation:
Such a triangle does not exist whose 
sides are 1,3 and 1 respectively.Thus,Area is
0.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function findArea() which takes three integers A,B and C as input parameters and returns the area of the triangle formed by the three integers as sides.
Note: Output the answer upto 3 decimal points
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=A,B,C,<=10^{4}
"""

from math import sqrt

def calculate_triangle_area(A: int, B: int, C: int) -> float:
    # Check if the sides can form a triangle
    if A + B > C and A + C > B and B + C > A:
        # Calculate the semi-perimeter
        s = (A + B + C) / 2
        # Calculate the area using Heron's formula
        area = sqrt(s * (s - A) * (s - B) * (s - C))
        # Return the area rounded to 3 decimal points
        return round(area, 3)
    else:
        # Return 0.0 if the triangle cannot be formed
        return 0.0