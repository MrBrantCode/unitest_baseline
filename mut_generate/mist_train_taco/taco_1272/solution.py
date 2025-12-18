"""
QUESTION:
Little Petya very much likes rectangles and especially squares. Recently he has received 8 points on the plane as a gift from his mother. The points are pairwise distinct. Petya decided to split them into two sets each containing 4 points so that the points from the first set lay at the vertexes of some square and the points from the second set lay at the vertexes of a rectangle. Each point of initial 8 should belong to exactly one set. It is acceptable for a rectangle from the second set was also a square. If there are several partitions, Petya will be satisfied by any of them. Help him find such partition. Note that the rectangle and the square from the partition should have non-zero areas. The sides of the figures do not have to be parallel to the coordinate axes, though it might be the case.

Input

You are given 8 pairs of integers, a pair per line — the coordinates of the points Petya has. The absolute value of all coordinates does not exceed 104. It is guaranteed that no two points coincide.

Output

Print in the first output line "YES" (without the quotes), if the desired partition exists. In the second line output 4 space-separated numbers — point indexes from the input, which lie at the vertexes of the square. The points are numbered starting from 1. The numbers can be printed in any order. In the third line print the indexes of points lying at the vertexes of a rectangle in the similar format. All printed numbers should be pairwise distinct.

If the required partition does not exist, the first line should contain the word "NO" (without the quotes), after which no output is needed.

Examples

Input

0 0
10 11
10 0
0 11
1 1
2 2
2 1
1 2


Output

YES
5 6 7 8
1 2 3 4


Input

0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7


Output

NO


Input

0 0
4 4
4 0
0 4
1 2
2 3
3 2
2 1


Output

YES
1 2 3 4
5 6 7 8

Note

Pay attention to the third example: the figures do not necessarily have to be parallel to the coordinate axes.
"""

import itertools
import math

def find_square_and_rectangle_partition(points):
    eps = 1e-08
    idx = list(range(8))

    def perpendicular(v1, v2):
        return sum([x * y for (x, y) in zip(v1, v2)]) < eps

    def all_perpendicular(vs):
        return all([perpendicular(vs[i], vs[(i + 1) % 4]) for i in range(4)])

    def rect_sides(vs):
        ls = list(map(lambda v: math.hypot(*v), vs))
        return abs(ls[0] - ls[2]) < eps and abs(ls[1] - ls[3]) < eps

    def square_sides(vs):
        ls = list(map(lambda v: math.hypot(*v), vs))
        l = ls[0]
        for lx in ls:
            if abs(lx - l) > eps:
                return False
        return True

    def coords_to_vecs(cs):
        return [[cs[(i + 1) % 4][0] - cs[i][0], cs[(i + 1) % 4][1] - cs[i][1]] for i in range(4)]

    def is_square(coords):
        for p in itertools.permutations(coords):
            vs = coords_to_vecs(p)
            if all_perpendicular(vs) and square_sides(vs):
                return True
        return False

    def is_rect(coord):
        for p in itertools.permutations(coord):
            vs = coords_to_vecs(p)
            if all_perpendicular(vs) and rect_sides(vs):
                return True
        return False

    for comb in itertools.combinations(idx, 4):
        fsi = list(comb)
        ssi = list(set(idx) - set(comb))
        fs = [points[i] for i in fsi]
        ss = [points[i] for i in ssi]
        if is_square(fs) and is_rect(ss):
            return [i + 1 for i in fsi], [i + 1 for i in ssi]
        if is_square(ss) and is_rect(fs):
            return [i + 1 for i in ssi], [i + 1 for i in fsi]
    
    return None