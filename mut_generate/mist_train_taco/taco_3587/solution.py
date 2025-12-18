"""
QUESTION:
Given the coordinates of the endpoints(p1-q1 and p2-q2) of the two line-segments. Check if they intersect or not.
Example 1:
Input:
p1=(1,1)
q1=(10,1)
p2=(1,2)
q2=(10,2)
Output:
0
Explanation:
The two line segments formed 
by p1-q1 and p2-q2 do not intersect.
Example 2:
Input:
p1=(10,0)
q1=(0,10)
p2=(0,0)
q2=(10,10)
Output:
1
Explanation:
The two line segments formed 
by p1-q1 and p2-q2 intersect.
Your Task:
You don't need to read input or print anything. Your task is to complete the function doIntersect() which takes the four points as input parameters and returns 1 if the line segments intersect. Otherwise, it returns 0.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
 
Constraints:
-10^{6}<=X,Y(for all points)<=10^{6}
"""

def do_segments_intersect(p1, q1, p2, q2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        if val > 0:
            return 1
        return 2

    def on_segment(p, q, r):
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return 1

    if o1 == 0 and on_segment(p1, p2, q1):
        return 1

    if o2 == 0 and on_segment(p1, q2, q1):
        return 1

    if o3 == 0 and on_segment(p2, p1, q2):
        return 1

    if o4 == 0 and on_segment(p2, q1, q2):
        return 1

    return 0