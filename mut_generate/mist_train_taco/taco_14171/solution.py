"""
QUESTION:
There are $n$ points on the plane, $(x_1,y_1), (x_2,y_2), \ldots, (x_n,y_n)$.

You need to place an isosceles triangle with two sides on the coordinate axis to cover all points (a point is covered if it lies inside the triangle or on the side of the triangle). Calculate the minimum length of the shorter side of the triangle.


-----Input-----

First line contains one integer $n$ ($1 \leq n \leq 10^5$).

Each of the next $n$ lines contains two integers $x_i$ and $y_i$ ($1 \leq x_i,y_i \leq 10^9$).


-----Output-----

Print the minimum length of the shorter side of the triangle. It can be proved that it's always an integer.


-----Examples-----
Input
3
1 1
1 2
2 1

Output
3
Input
4
1 1
1 2
2 1
2 2

Output
4


-----Note-----

Illustration for the first example: [Image]

Illustration for the second example: [Image]
"""

def minimum_triangle_side_length(points):
    """
    Calculate the minimum length of the shorter side of an isosceles triangle with two sides on the coordinate axis
    that covers all given points.

    Parameters:
    points (list of tuples): A list of points on the plane, where each point is represented as a tuple (x_i, y_i).

    Returns:
    int: The minimum length of the shorter side of the triangle.
    """
    # Calculate the sum of coordinates for each point
    side_lengths = [x + y for x, y in points]
    
    # The minimum length of the shorter side is the maximum of these sums
    return max(side_lengths)