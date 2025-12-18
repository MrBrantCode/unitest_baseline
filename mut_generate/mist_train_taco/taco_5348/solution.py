"""
QUESTION:
Consider a 2d-grid. That is, each cell is identified by (i,j). You have received reports of two snake-sightings on this grid. You want to check whether they could be partial sightings of the same snake or not.
Each of the snake sightings correspond to a straight, axis-parallel line segment in the grid, and the starting and ending cells for each are given to you. Now consider a graph, where each cell in the 2d-grid is a vertex. And there is an edge between 2 vertices if and only if the cells corresponding to these two vertices are consecutive cells in at least one of the two snakes. That is, at least in one of the snakes, when you go from one end point to the other end point, these two cells should occur consecutively.
The two sightings/snakes are said to be same, if both these conditions are satisfied:
- The union of the set of cells in the first snake and the set of cells in the second snake, should form a connected component in this graph.
- No vertex should have degree more than 2 in the graph.
In other words, the induced subgraph on the union set must be a path graph.

-----Input-----
- The first line contains a single integer, T, which is the number of testcases. The description of each testcase follows.
- The first line of each testcase contains four integers: X11, Y11, X12, Y12. This represents the fact that the first snake's end points are (X11, Y11) and (X12, Y12).
- The second line of each testcase contains four integers: X21, Y21, X22, Y22. This represents the fact that the second snake's end points are (X21, Y21) and (X22, Y22).

-----Output-----
- For each testcase, output "yes" if the snakes are the same, as per the definition given above. Output "no" otherwise.

-----Constraints-----
- 1 ≤ T ≤ 105
- -109 ≤ Xij,Yij ≤ 109
- The two end points of every snake is guaranteed to be either on the same row or on the same column. Thus, the snake occupies all the cells between these cells, including the end points.

-----Example-----
Input:
4
2 1 8 1
11 1 7 1
2 1 8 1
11 1 9 1
2 1 8 1
3 1 3 -2
2 1 8 1
2 1 2 -2
Output:
yes
no
no
yes

-----Explanation-----
In the images, the first snake is red, the second snake is yellow, and the intersections, if any, are in orange.
The first test case corresponds to:

Both the conditions on the graph are satisfied, and hence this is a "yes".
The second test case corresponds to:

There is no edge between the vertex corresponding to the (8,1) cell and the vertex corresponding to (9,1), Hence, the union set is disconnected, and thus the answer is "no". 
The third test case corresponds to:

The vertex corresponding to the cell (3,1) has degree 3, which is more than 2, and thus the answer is "no". 
The fourth test case corresponds to:

Both the conditions on the graph are satisfied, and hence this is a "yes".
"""

def are_snakes_same(x11, y11, x12, y12, x21, y21, x22, y22):
    """
    Determines if two snake sightings could be partial sightings of the same snake.

    Parameters:
    - x11, y11: Coordinates of the first endpoint of the first snake.
    - x12, y12: Coordinates of the second endpoint of the first snake.
    - x21, y21: Coordinates of the first endpoint of the second snake.
    - x22, y22: Coordinates of the second endpoint of the second snake.

    Returns:
    - bool: True if the snakes are the same, False otherwise.
    """
    if (x11 == x21 and y11 == y21) or (x12 == x22 and y12 == y22):
        return True
    elif (x11 == x22 and y11 == y22) or (x12 == x21 and y12 == y21):
        return True
    elif y11 == y12 and y11 == y21 and y11 == y22:
        a1 = max(x11, x12)
        a2 = min(x11, x12)
        b1 = max(x21, x22)
        b2 = min(x21, x22)
        if a1 >= b2 and a2 <= b1:
            return True
        else:
            return False
    elif x11 == x12 and x11 == x21 and x11 == x22:
        a1 = max(y11, y12)
        a2 = min(y11, y12)
        b1 = max(y21, y22)
        b2 = min(y21, y22)
        if a1 >= b2 and a2 <= b1:
            return True
        else:
            return False
    else:
        return False