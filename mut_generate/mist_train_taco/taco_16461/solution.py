"""
QUESTION:
You are given three points a(a1, a2), b(b1, b2) and c(c1, c2) on a page. Find if it’s possible to rotate the page in any direction by any angle, such that the new position of a is same as the old position of b, and the new position of b is same as the old position of c. 
Example 1:
Input: 
a1 = 1, a2 = 1
b1 = 1, b2 = 1
c1 = 1, c2 = 0
Output: 0
Explanation: Not possible.
Example 2:
Input: 
a1 = 0, a2 = 1
b1 = 1, b2 = 1
c1 = 1, c2 = 0
Output: 1
Explanation: Rotate the page by 90 degree.
Your Task:  
You dont need to read input or print anything. Complete the function possibleOrNot() which takes a1, a2, b1, b2, c1 and c2 as input parameters and returns 1 if it is possible to rotate the page or 0 otherwise. 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
0 ≤ a1, a2, b1, b2, c1, c2 ≤ 100
"""

import math

def is_rotation_possible(a1, a2, b1, b2, c1, c2):
    d1 = math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
    d2 = math.sqrt((b1 - c1) ** 2 + (b2 - c2) ** 2)
    if d1 == d2:
        return 1
    else:
        return 0