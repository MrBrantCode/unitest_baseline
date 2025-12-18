"""
QUESTION:
A renowned abstract artist Sasha, drawing inspiration from nowhere, decided to paint a picture entitled "Special Olympics". He justly thought that, if the regular Olympic games have five rings, then the Special ones will do with exactly two rings just fine.

Let us remind you that a ring is a region located between two concentric circles with radii r and R (r < R). These radii are called internal and external, respectively. Concentric circles are circles with centers located at the same point.

Soon a white canvas, which can be considered as an infinite Cartesian plane, had two perfect rings, painted with solid black paint. As Sasha is very impulsive, the rings could have different radii and sizes, they intersect and overlap with each other in any way. We know only one thing for sure: the centers of the pair of rings are not the same.

When Sasha got tired and fell into a deep sleep, a girl called Ilona came into the room and wanted to cut a circle for the sake of good memories. To make the circle beautiful, she decided to cut along the contour.

We'll consider a contour to be a continuous closed line through which there is transition from one color to another (see notes for clarification). If the contour takes the form of a circle, then the result will be cutting out a circle, which Iona wants.

But the girl's inquisitive mathematical mind does not rest: how many ways are there to cut a circle out of the canvas?

Input

The input contains two lines. 

Each line has four space-separated integers xi, yi, ri, Ri, that describe the i-th ring; xi and yi are coordinates of the ring's center, ri and Ri are the internal and external radii of the ring correspondingly ( - 100 ≤ xi, yi ≤ 100; 1 ≤ ri < Ri ≤ 100). 

It is guaranteed that the centers of the rings do not coinside.

Output

A single integer — the number of ways to cut out a circle from the canvas.

Examples

Input

60 60 45 55
80 80 8 32


Output

1

Input

60 60 45 55
80 60 15 25


Output

4

Input

50 50 35 45
90 50 35 45


Output

0

Note

Figures for test samples are given below. The possible cuts are marked with red dotted line. 

<image> <image> <image>
"""

def count_ways_to_cut_circle(ring1, ring2):
    def intersect(a, b):
        d2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        r1r22 = (a[2] + b[2]) ** 2
        dr1r22 = (a[2] - b[2]) ** 2
        return dr1r22 < d2 < r1r22

    def lies(a, b, c):
        d2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        return max(0, b[2] - a[2]) ** 2 < d2 <= max(0, c[2] - a[2]) ** 2

    a = [
        (ring1[0], ring1[1], ring1[2]),
        (ring1[0], ring1[1], ring1[3]),
        (ring2[0], ring2[1], ring2[2]),
        (ring2[0], ring2[1], ring2[3])
    ]

    ans = 0
    for i in range(4):
        f = 0
        for j in range(4):
            if i != j and intersect(a[i], a[j]):
                f = 1
        if i < 2:
            if lies(a[i], a[2], a[3]):
                f = 1
        elif lies(a[i], a[0], a[1]):
            f = 1
        if f == 0:
            ans += 1

    return ans