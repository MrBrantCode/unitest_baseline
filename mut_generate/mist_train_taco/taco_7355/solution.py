"""
QUESTION:
Given two points P(a, b) and Q(c, d) in the coordinate plane, find the equation of the line passing through both the points.
Example 1:
Input: P = (3, 2)
Q = (2, 6)
Output: 4x+1y=14
Explaination: Using the formula to get
line equation from two points we can
get it.
Example 2:
Input: P = (3, 2)
Q = (5, 7)
Output: 5x-2y=11
Explaination: If we use the formula to
get line equation from two points we
get this equation.
Your Task:
You do not need to read input or print anything. Your task is to complete the function getLine() which takes the values a, b, c and d as input parameters and returns a string which represents the equation.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a, b, c, d ≤ 10^{5}
"""

def get_line_equation(a, b, c, d):
    x = d - b
    y = c - a
    z = (d - b) * a - (c - a) * b
    
    if x > 0:
        if y > 0:
            return f"{x}x-{y}y={z}"
        return f"{x}x+{abs(y)}y={z}"
    if y > 0:
        return f"{x}x-{y}y={z}"
    return f"{x}x+{abs(y)}y={z}"