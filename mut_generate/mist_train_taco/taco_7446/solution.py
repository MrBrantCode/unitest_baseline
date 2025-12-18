"""
QUESTION:
You are given the following points with integer coordinates on the plane: M0, A0, A1, ..., An - 1, where n is odd number. Now we define the following infinite sequence of points Mi: Mi is symmetric to Mi - 1 according <image> (for every natural number i). Here point B is symmetric to A according M, if M is the center of the line segment AB. Given index j find the point Mj.

Input

On the first line you will be given an integer n (1 ≤ n ≤ 105), which will be odd, and j (1 ≤ j ≤ 1018), where j is the index of the desired point. The next line contains two space separated integers, the coordinates of M0. After that n lines follow, where the i-th line contain the space separated integer coordinates of the point Ai - 1. The absolute values of all input coordinates will not be greater then 1000.

Output

On a single line output the coordinates of Mj, space separated.

Examples

Input

3 4
0 0
1 1
2 3
-5 3


Output

14 0


Input

3 1
5 5
1000 1000
-1000 1000
3 100


Output

1995 1995
"""

def find_symmetric_point(n, j, m0, points_a):
    # Extract the initial coordinates of M0
    mx, my = m0
    
    # Extract the coordinates of points A
    ax = [point[0] for point in points_a]
    ay = [point[1] for point in points_a]
    
    # Reduce the index j modulo 2 * n
    k = j % (2 * n)
    
    # Compute the coordinates of Mj
    for i in range(k):
        mx = 2 * ax[i % n] - mx
        my = 2 * ay[i % n] - my
    
    return (mx, my)