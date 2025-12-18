"""
QUESTION:
Given the coordinates of the centres of two circles (X1, Y1) and (X2, Y2) as well as the radii of the respective circles R1 and R2.Find the floor of the area of their intersection.
Note: Use the value of Pi as 3.14
Example 1:
Input:
X1=0,Y1=0,R1=4
X2=6,Y2=0,R2=4
Output:
7
Explanation:
The intersecting area equals 7.25298806.
So,Answer is 7.
Example 2:
Input:
X1=0,Y1=0,R1=5
X2=11,Y2=0,R2=5
Output:
0
Explanation:
The circles don't intersect.
Your Task:
You don't need to read input or print anything. Your task is to complete the function intersectionArea() which takes the coordinates of the centers as well as the radii(X1, Y1, R1, X2, Y2, R2) as input parameters and returns the area of intersection of the two circles.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
-10^{9}<=X1,Y1,X2,Y2<=10^{9}
1<=R1,R2<=10^{9}
"""

import math

def calculate_intersection_area(X1, Y1, R1, X2, Y2, R2):
    D = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
    if D > R1 + R2:
        return 0
    elif D < abs(R1 - R2):
        return math.floor(min(R1, R2) ** 2 * 3.14)
    else:
        a = (R1 ** 2 - R2 ** 2 + D ** 2) / (2 * D)
        b = D - a
        c = math.sqrt(R1 ** 2 - a ** 2)
        area = (R1 ** 2 * math.acos(a / R1) - a * c + 
                R2 ** 2 * math.acos(b / R2) - b * math.sqrt(R2 ** 2 - b ** 2))
        return math.floor(area)