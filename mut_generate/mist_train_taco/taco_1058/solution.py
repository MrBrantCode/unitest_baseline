"""
QUESTION:
Given an integer R which represents the radius of a circle that has (0,0) as its centre, find the total number of lattice points on the circumference. Lattice Points are points with coordinates as integers in 2-D space.
Example 1:
Input: R = 5
Output: 12
Explanation: (0,5), (0,-5), (5,0), 
(-5,0), (3,4), (-3,4), (-3,-4), (3,-4), 
(4,3), (-4,3), (-4,-3), (4,-3).
Example 2:
Input: R = 88
Output: 4
Explanation: (0,88), (88,0), (0,-88), 
(-88,0)
Your Task:  
You don't need to read input or print anything. Your task is to complete the function latticePoints() which takes R as input and returns the number of lattice points.
Expected Time Complexity: O(RsqrtR)
Expected Auxiliary Space: O(1)
Constraints:
0 ≤ R ≤ 10^{4}
"""

import math

def count_lattice_points(R: int) -> int:
    if R == 0:
        return 0
    
    count = 4  # Initial count for (0, R), (0, -R), (R, 0), (-R, 0)
    
    for i in range(1, R):
        t = math.sqrt(R * R - i * i)
        if t == int(t):
            count += 4
    
    return count