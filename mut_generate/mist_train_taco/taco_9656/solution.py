"""
QUESTION:
Given four different points in space. Find whether these points can form a square or not.
 
Example 1:
Input:
x1 = 20, y1 = 10, x2 = 10, y2 = 20, 
x3 = 20, y3 = 20, x4 = 10, y4 = 10 
Output:
Yes
Explanation:
The points (20,10), (10,20), (20,20),
(10,10) forms a square.
Example 2:
Input:
x1 = 2, y1 = 1, x2 = 10, y2 = 20, 
x3 = 5, y3 = 6, x4 = 10, y4 = 10 
Output:
No
Explanation:
The points (2,1), (10,20), (5,6),
(10,10) doesn't form a square.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSquare() which takes 8 Integers x1, y1, x2, y2, x3, y3, x4, and y4 as input and returns whether these points form a square.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
-10^{3} ≤ x1, y1, x2, y2, x3, y3, x4, y4 ≤ 10^{3}
"""

def is_square(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate the squared distances between all pairs of points
    def dist_sq(x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    distances = [
        dist_sq(x1, y1, x2, y2),
        dist_sq(x1, y1, x3, y3),
        dist_sq(x1, y1, x4, y4),
        dist_sq(x2, y2, x3, y3),
        dist_sq(x2, y2, x4, y4),
        dist_sq(x3, y3, x4, y4)
    ]
    
    # Sort the distances to easily check for square properties
    distances.sort()
    
    # For the points to form a square:
    # - There should be four equal shortest distances (sides)
    # - There should be two equal longer distances (diagonals)
    return (distances[0] > 0 and
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5] and
            distances[4] == 2 * distances[0])