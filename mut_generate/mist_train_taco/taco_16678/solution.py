"""
QUESTION:
Given a circular sheet of radius, R. Find the total number of rectangles with integral length and width that can be cut from the sheet, one at a time.
Example 1:
Input:
R=1
Output:
1
Explanation:
Only 1 rectangle of dimensions 1x1.
Example 2:
Input:
R=2
Output:
8
Explanation:
The 8 possible rectangles are 
(1x1)(1x2)(1x3)(2x1)(2x2)(2x3)(3x1)(3x2).
Your Task:
You don't need to read input or print anything. Your task is to complete the function rectanglesInCircle() which takes an integer R as the radius and returns the number of rectangles that can fit on the circle.
Expected Time Complexity:O(R^{2})
Expected Auxillary Space:O(1)
Constraints:
1<=R<=1000
"""

def rectangles_in_circle(R: int) -> int:
    rec = 0
    d = 2 * R
    ds = d * d
    for i in range(1, 2 * R):
        for j in range(1, 2 * R):
            dl = i * i + j * j
            if dl <= ds:
                rec += 1
    return rec