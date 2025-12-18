"""
QUESTION:
A mobile phone company ACMICPC (Advanced Cellular, Mobile, and Internet-Connected Phone Corporation) is planning to set up a collection of antennas for mobile phones in a city called Maxnorm. The company ACMICPC has several collections for locations of antennas as their candidate plans, and now they want to know which collection is the best choice.

for this purpose, they want to develop a computer program to find the coverage of a collection of antenna locations. Each antenna Ai has power ri, corresponding to "radius". Usually, the coverage region of the antenna may be modeled as a disk centered at the location of the antenna (xi, yi) with radius ri. However, in this city Maxnorm such a coverage region becomes the square [xi − ri, xi + ri] × [yi − ri, yi + ri]. In other words, the distance between two points (xp, yp) and (xq, yq) is measured by the max norm max{ |xp − xq|, |yp − yq|}, or, the L∞ norm, in this city Maxnorm instead of the ordinary Euclidean norm √ {(xp − xq)2 + (yp − yq)2}.

As an example, consider the following collection of 3 antennas


4.0 4.0 3.0
5.0 6.0 3.0
5.5 4.5 1.0


depicted in the following figure

<image>

where the i-th row represents xi, yi ri such that (xi, yi) is the position of the i-th antenna and ri is its power. The area of regions of points covered by at least one antenna is 52.00 in this case.

Write a program that finds the area of coverage by a given collection of antenna locations.



Input

The input contains multiple data sets, each representing a collection of antenna locations. A data set is given in the following format.



n
x1 y1 r1
x2 y2 r2
. . .
xn yn rn



The first integer n is the number of antennas, such that 2 ≤ n ≤ 100. The coordinate of the i-th antenna is given by (xi, yi), and its power is ri. xi, yi and ri are fractional numbers between 0 and 200 inclusive.

The end of the input is indicated by a data set with 0 as the value of n.

Output

For each data set, your program should output its sequence number (1 for the first data set, 2 for the second, etc.) and the area of the coverage region. The area should be printed with two digits to the right of the decimal point, after rounding it to two decimal places.

The sequence number and the area should be printed on the same line with no spaces at the beginning and end of the line. The two numbers should be separated by a space.

Example

Input

3
4.0 4.0 3.0
5.0 6.0 3.0
5.5 4.5 1.0
2
3.0 3.0 3.0
1.5 1.5 1.0
0


Output

1 52.00
2 36.00
"""

from bisect import bisect_left

def calculate_coverage_area(antenna_data):
    cno = 1  # Sequence number
    n = len(antenna_data)
    
    if n == 0:
        return cno, 0.00
    
    tbl, xx, yy = [], set(), set()
    
    for (x, y, r) in antenna_data:
        x, y, r = int(100 * x), int(100 * y), int(100 * r)
        x1, y1, x2, y2 = x - r, y - r, x + r, y + r
        tbl.append((x1, y1, x2, y2))
        xx.add(x1)
        xx.add(x2)
        yy.add(y1)
        yy.add(y2)
    
    xx = sorted(xx)
    yy = sorted(yy)
    arr = [[0 for _ in range(201)] for _ in range(201)]
    
    for (x1, y1, x2, y2) in tbl:
        l = bisect_left(xx, x1)
        r = bisect_left(xx, x2)
        u = bisect_left(yy, y1)
        d = bisect_left(yy, y2)
        for y in range(u, d):
            for x in range(l, r):
                arr[y][x] = 1
    
    ans = 0
    for r in range(1, len(yy)):
        t = yy[r] - yy[r - 1]
        for c in range(1, len(xx)):
            if arr[r - 1][c - 1]:
                ans += t * (xx[c] - xx[c - 1])
    
    ans //= 100
    coverage_area = ans / 100.0
    
    return cno, f"{coverage_area:.2f}"