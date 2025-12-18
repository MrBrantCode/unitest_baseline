"""
QUESTION:
Given three corner points of a triangle(with coordinates (x1,y1), (x2,y2), and (x3,y3)), and one more point P. Write a function to check whether P lies within the triangle or not.
 
Example 1:
Input:
x1 = 0, y1 = 0, x2 = 20, y2 = 0, 
x3 = 10, y3 = 30, x = 10, y = 15
Output:
Yes
Explanation:
The point (x,y) lies within the 
Triangle.
Example 2:
Input:
x1 = 0, y1 = 0, x2 = 20, y2 = 20, 
x3 = 20, y3 = 0, x = 30, y = 0
Output:
No
Explanation:
The point (x,y) doesn't lie within the Triangle.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isInsideTri() which takes eight Integers x1,x2,x3,y1,y2,y3,x, and y as input and returns "Yes" if the Point lies inside the Triangle else returns "No".
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ x1,x2,x3,y1,y2,y3 ≤ 10^{4}
1 ≤ x,y ≤ 10^{4}
"""

def is_point_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    ABC = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    PAB = (x * (y1 - y2) + x1 * (y2 - y) + x2 * (y - y1)) / 2
    PAC = (x * (y1 - y3) + x1 * (y3 - y) + x3 * (y - y1)) / 2
    PBC = (x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2
    
    if abs(ABC) == abs(PAB) + abs(PAC) + abs(PBC):
        return 'Yes'
    return 'No'