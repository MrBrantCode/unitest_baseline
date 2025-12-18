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

from math import sqrt, asin, degrees

def is_square(x1, y1, x2, y2, x3, y3, x4, y4):
    b = sorted([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    (x1, y1) = b[0]
    (x2, y2) = b[1]
    (x3, y3) = b[2]
    (x4, y4) = b[3]
    a1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    a2 = sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
    a3 = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    a4 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    return a1 == a2 == a3 == a4 and a1 != 0 and (a4 != 0) and (abs(abs(degrees(asin((y2 - y1) / a1) - asin((y3 - y1) / a4))) - 90) <= 10 ** (-8))

def is_rectangle(x1, y1, x2, y2, x3, y3, x4, y4):
    b = sorted([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    (x1, y1) = b[0]
    (x2, y2) = b[1]
    (x3, y3) = b[2]
    (x4, y4) = b[3]
    a1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    a2 = sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
    a3 = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    a4 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    return a1 == a3 and a2 == a4 and (a1 != 0) and (a4 != 0) and (abs(abs(degrees(asin((y2 - y1) / a1) - asin((y3 - y1) / a4))) - 90) <= 10 ** (-8))

def find_square_and_rectangle(points):
    for i in range(5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                for l in range(k + 1, 8):
                    if is_square(*points[i] + points[j] + points[k] + points[l]):
                        remaining_points = []
                        remaining_indices = []
                        for m in range(8):
                            if m not in [i, j, k, l]:
                                remaining_points += points[m]
                                remaining_indices.append(m + 1)
                        if is_rectangle(*remaining_points):
                            square_indices = [i + 1, j + 1, k + 1, l + 1]
                            return (square_indices, remaining_indices)
    return None