"""
QUESTION:
Rachel, being an awesome android programmer, just finished an App that will let us draw a triangle by selecting three points on the touch-plane.Now She asks her friend Bruce to draw a Right-Angled Triangle (we'll call it RAT) by selecting 3 integral points on the plane.
 A RAT is a triangle with Non-Zero area and a right-angle.

But Bruce, being in a hurry as always, makes a mistake on drawing the points. Now Rachel's app can fix Bruce's mistake if only one coordinate of any one point can be adjusted within a distance of 1 units. i.e., if the drawn triangle can be made a RAT by adjusting any one coordinate within 1 unit of distance.

Your task is simple, given 6 coordinates (each Integer pair representing a point), you have to tell can Rachel's app correct Bruce's mistake automatically?

Input:

      First line containing T, the number of test cases.
      Then T lines follow with 6 space separated coordinates.

Output:

      print "YES" in a newline if it's possible.
      otherwise print "NO" in a newline.

Constraints:

      1 ≤ T ≤ 100
      -1000 ≤ xi,yi ≤ 1000

SAMPLE INPUT
3
-1 0 2 0 0 1
2 3 4 5 6 6
0 0 2 0 10 10

SAMPLE OUTPUT
YES
NO
NO

Explanation

Case 1:  For (-1, 0), (2, 0) and (0, 1), shifting (-1, 0) to (0, 0) makes it a RAT. 

Case 2 and Case 3:   No any possible shift results into a RAT.

Note that any point can be moved either in x- or in y- direction at a time by 1 unit.
"""

def dist(x1, y1, x2, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

def is_RAT(a):
    ab = dist(a[0], a[1], a[2], a[3])
    bc = dist(a[4], a[5], a[2], a[3])
    ca = dist(a[0], a[1], a[4], a[5])
    if ab == bc + ca or ca == bc + ab or bc == ab + ca:
        return True
    return False

def samepoint(a):
    if a[0] == a[2] and a[1] == a[3]:
        return True
    if a[0] == a[4] and a[1] == a[5]:
        return True
    if a[4] == a[2] and a[5] == a[3]:
        return True
    return False

def can_correct_to_right_angled_triangle(points):
    d = [0, -1, +1]
    found = False
    for diff in d:
        for i in range(0, 6):
            points[i] = points[i] + diff
            if is_RAT(points) and not samepoint(points):
                found = True
                break
            points[i] = points[i] - diff
        if found:
            break
    return "YES" if found else "NO"