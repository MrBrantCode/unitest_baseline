"""
QUESTION:
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True



 Note: 

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""

def is_valid_square(p1, p2, p3, p4):
    def length(x, y):
        return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])
    
    res = []
    a1 = length(p1, p2)
    a2 = length(p1, p3)
    a3 = length(p1, p4)
    a4 = length(p2, p3)
    a5 = length(p2, p4)
    a6 = length(p3, p4)
    res = [a1, a2, a3, a4, a5, a6]
    res = sorted(res)
    
    for i in range(3):
        if res[i] == res[i + 1]:
            continue
        else:
            return False
    
    if res[4] != res[5]:
        return False
    
    if res[0] != 0:
        return True
    else:
        return False