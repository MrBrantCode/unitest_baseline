"""
QUESTION:
I am a craftsman specialized in interior works. A customer asked me to perform wiring work on a wall whose entire rectangular surface is tightly pasted with pieces of panels. The panels are all of the same size (2 m in width, 1 m in height) and the wall is filled with an x (horizontal) by y (vertical) array of the panels. The customer asked me to stretch a wire from the left top corner of the wall to the right bottom corner whereby the wire is tied up at the crossing points with the panel boundaries (edges and vertexes) as shown in the figure. There are nine tied-up points in the illustrative figure shown below.

<image>
Fig: The wire is tied up at the edges and vertexes of the panels (X: 4 panels, Y: 6 panels)



Write a program to provide the number of points where the wire intersects with the panel boundaries. Assume that the wire and boundary lines have no thickness.



Input

The input is given in the following format.


x y


A line of data is given that contains the integer number of panels in the horizontal direction x (1 ≤ x ≤ 1000) and those in the vertical direction y (1 ≤ y ≤ 1000).

Output

Output the number of points where the wire intersects with the panel boundaries.

Examples

Input

4 4


Output

5


Input

4 6


Output

9
"""

def calculate_wire_intersections(x: int, y: int) -> int:
    cnt = 0
    for i in range(0, x * 2 + 1, 2):
        if y * i % (2 * x) == 0:
            cnt += 1
    return x + y - cnt + 2