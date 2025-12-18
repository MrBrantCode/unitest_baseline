"""
QUESTION:
Guy-Manuel and Thomas are going to build a polygon spaceship.

You're given a strictly convex (i. e. no three points are collinear) polygon P which is defined by coordinates of its vertices. Define P(x,y) as a polygon obtained by translating P by vector \overrightarrow {(x,y)}. The picture below depicts an example of the translation:

<image>

Define T as a set of points which is the union of all P(x,y) such that the origin (0,0) lies in P(x,y) (both strictly inside and on the boundary). There is also an equivalent definition: a point (x,y) lies in T only if there are two points A,B in P such that \overrightarrow {AB} = \overrightarrow {(x,y)}. One can prove T is a polygon too. For example, if P is a regular triangle then T is a regular hexagon. At the picture below P is drawn in black and some P(x,y) which contain the origin are drawn in colored: 

<image>

The spaceship has the best aerodynamic performance if P and T are similar. Your task is to check whether the polygons P and T are [similar](https://tinyurl.com/vp5m7vl).

Input

The first line of input will contain a single integer n (3 ≤ n ≤ 10^5) — the number of points.

The i-th of the next n lines contains two integers x_i, y_i (|x_i|, |y_i| ≤ 10^9), denoting the coordinates of the i-th vertex.

It is guaranteed that these points are listed in counterclockwise order and these points form a strictly convex polygon.

Output

Output "YES" in a separate line, if P and T are similar. Otherwise, output "NO" in a separate line. You can print each letter in any case (upper or lower).

Examples

Input


4
1 0
4 1
3 4
0 3


Output


YES

Input


3
100 86
50 0
150 0


Output


nO

Input


8
0 0
1 0
2 1
3 3
4 6
3 6
2 5
1 3


Output


YES

Note

The following image shows the first sample: both P and T are squares. The second sample was shown in the statements.

<image>
"""

def are_polygons_similar(n, vertices):
    def vt(p1, p2):
        return [p2[0] - p1[0], p2[1] - p1[1]]

    def isSame(vt1, vt2):
        if vt1[0] == vt2[0] and vt1[1] == vt2[1]:
            return True
        if vt1[0] == -vt2[0] and vt1[1] == -vt2[1]:
            return True
        return False

    # Append the first vertex to the end to close the polygon
    vertices.append(vertices[0])

    # If the number of vertices is odd, P and T cannot be similar
    if n % 2 == 1:
        return "NO"

    # Check the similarity condition
    for i in range(n // 2):
        vt1 = vt(vertices[i], vertices[i + 1])
        vt2 = vt(vertices[i + n // 2], vertices[i + n // 2 + 1])
        if not isSame(vt1, vt2):
            return "NO"

    return "YES"