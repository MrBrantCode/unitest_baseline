"""
QUESTION:
Everyone knows what a square looks like. Mathematically, a square is a regular quadrilateral. This means that it has four equal sides and four equal angles (90 degree angles).
One beautiful day, Johnny eagerly examined the interesting properties of squares. He did not forget you, his best friend and a talented programmer and thus made a problem about squares to challenge your programming ability. The problem is: given a set of N points in the plane, how many squares are there such that all their corners belong to this set?
Now let's show Johnny your skill!

------ Input ------ 

The first line contains t, the number of test cases (about 10). Then t test cases follow.
Each test case has the following form:
The first line contains an integer N, the number of points in the given set (4 ≤ N ≤ 500).
Then N lines follow, each line contains two integers X, Y describing coordinates of a point (-50 ≤ X, Y ≤ 50).

------ Output ------ 

For each test case, print in a single line the number of squares that have vertices belong to the given set.

----- Sample Input 1 ------ 
1
7
0 0
0 1
1 0
1 1
1 2
2 1
2 2
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
The three squares are: (0 0), (0 1), (1 1), (1 0)(1 1), (1 2), (2 2), (2 1)(0 1), (1 0), (2 1), (1 2)
"""

def count_squares_in_points(points):
    """
    Counts the number of squares that can be formed using the given points.

    Parameters:
    points (list of tuples): A list of tuples where each tuple represents the coordinates of a point.

    Returns:
    int: The number of squares that can be formed using the given points.
    """
    point_set = set(points)
    count = 0
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            
            # Check for the other two points to form a square
            if (x1 + dy, y1 - dx) in point_set and (x2 + dy, y2 - dx) in point_set:
                count += 1
            if (x1 - dy, y1 + dx) in point_set and (x2 - dy, y2 + dx) in point_set:
                count += 1
    
    return count // 4