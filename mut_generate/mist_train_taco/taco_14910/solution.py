"""
QUESTION:
On a two-dimensional plane, there are N red points and N blue points.
The coordinates of the i-th red point are (a_i, b_i), and the coordinates of the i-th blue point are (c_i, d_i).
A red point and a blue point can form a friendly pair when, the x-coordinate of the red point is smaller than that of the blue point, and the y-coordinate of the red point is also smaller than that of the blue point.
At most how many friendly pairs can you form? Note that a point cannot belong to multiple pairs.

-----Constraints-----
 - All input values are integers.
 - 1 \leq N \leq 100
 - 0 \leq a_i, b_i, c_i, d_i < 2N
 - a_1, a_2, ..., a_N, c_1, c_2, ..., c_N are all different.
 - b_1, b_2, ..., b_N, d_1, d_2, ..., d_N are all different.

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 b_1
a_2 b_2
:
a_N b_N
c_1 d_1
c_2 d_2
:
c_N d_N

-----Output-----
Print the maximum number of friendly pairs.

-----Sample Input-----
3
2 0
3 1
1 3
4 2
0 4
5 5

-----Sample Output-----
2

For example, you can pair (2, 0) and (4, 2), then (3, 1) and (5, 5).
"""

def max_friendly_pairs(N, red_points, blue_points):
    """
    Calculate the maximum number of friendly pairs that can be formed from red and blue points on a 2D plane.

    Parameters:
    - N (int): The number of red and blue points.
    - red_points (list of tuples): List of (a_i, b_i) coordinates for red points.
    - blue_points (list of tuples): List of (c_i, d_i) coordinates for blue points.

    Returns:
    - int: The maximum number of friendly pairs.
    """
    # Sort red points by y-coordinate in descending order
    red_points_sorted = sorted(red_points, key=lambda k: k[1], reverse=True)
    # Sort blue points by x-coordinate in ascending order
    blue_points_sorted = sorted(blue_points, key=lambda k: k[0])
    
    count = 0
    for (c, d) in blue_points_sorted:
        for i in range(len(red_points_sorted)):
            if c > red_points_sorted[i][0] and d > red_points_sorted[i][1]:
                red_points_sorted.pop(i)
                count += 1
                break
    
    return count