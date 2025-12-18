"""
QUESTION:
Given coordinates of four points in a plane. Find if the four points form a square or not.
Example 1:
Input:
points=(0,0),(0,1),(1,0),(1,1)
Output:
1
Explanation:
These points form a square.
Example 2:
Input:
points=(0,0),(1,1),(1,0),(0,2)
Output:
0
Explanation:
These four points do not form a square.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function fourPointSquare() which takes a 2D array of dimensions 4x2 which contains the cordinates of the four points and returns 1 if they form a square.Otherwise it returns 0.
 
Expected Time Complexity:O(1)
Expected Space Complexity:O(1)
 
Constraints:
0<=X-cordinate,Y-cordinate<=10^{5}
"""

def is_square(points):
    def distance(x, y):
        return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])
    
    record = dict()
    for i in range(4):
        for j in range(i + 1, 4):
            dist = distance(points[i], points[j])
            record[dist] = record.get(dist, 0) + 1
    
    if len(record) != 2:
        return 0
    
    for val in record.values():
        if not (val == 2 or val == 4):
            return 0
    
    return 1