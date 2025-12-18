"""
QUESTION:
*Jagdish Bhagat bolta hai... Gav se gav jod diya hai...  
The government is very upset with Mr. Bhagat's feedback and decided to directly connect every single pair of villages. Help the government solve this in minimum number of days.*

Aryan has N pairwise distinct points lying on the coordinate axes, i.e, every point is of the form (x, 0) or (0, y). Aryan wants to draw line segments connecting every pair of the given points.

In one second, Aryan can draw line segments between as many pairs of points as he likes, as long as all the segments drawn in this second do not intersect or overlap non-trivially with each other; however, it is allowed for the endpoint of one segment to touch another segment.  
That is, if two segments share a point, then that point must be the endpoint of at least one of the two segments. See the sample cases below for an example.

For example, Aryan cannot draw a segment joining (1, 0) to (0, 2) *and* a segment joining (2, 0) and (0, 1) in the same second, since they intersect. However, he can draw segments (0, 1)-(2, 0), (0, 0)-(0, 2) and (0, 1)-(1, 0) in the same second, since they only touch at an endpoint.

Find the minimum number of seconds Aryan needs to draw all the \binom{N}{2} line segments.

Note that every possible line segment must be drawn. That is, if you had the points \{(-1, 0), (0, 0), (1, 0)\}, then all three pairs of line segments must be drawn — it is not enough to draw the segment (-1, 0) - (1, 0).

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of testcases.
- Each testcase consists of multiple lines of input.
- The first line of each testcase contains a single integer N — the number of points on the coordinate axes.
- Each of the next N lines contains two space-separated integers x and y, denoting the point (x, y). It is guaranteed that at least one of x and y will be 0.

------ Output Format ------ 

For each testcase, output on a single line the minimum number of seconds Aryan needs to draw line segment between every pair of points.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 10^{6}$
$-10^{9} ≤ x , y ≤ 10^{9}$
- Every input point will lie on the coordinate axes.
- The input points are pairwise distinct.
- The sum of $N$ across all the testcases won't exceed $10^{6}$.

----- Sample Input 1 ------ 
3
5
0 0
0 1
0 2
2 0
1 0
5
-1 0
0 0
1 0
0 5
0 4
6
0 -1
1 0
-1 0
0 1
2 0
-2 0
----- Sample Output 1 ------ 
2
2
5
----- explanation 1 ------ 
Test case $1$: Let's denote the points as: $P_{1} \rightarrow (1,0)$ , $P_{2} \rightarrow (2,0)$ , $P_{3} \rightarrow (0,1)$ , $P_{4} \rightarrow (0,2)$ , $P_{5} \rightarrow (0,0)).$    
There are a total of $10$ line segments amongst these points.

These $10$ segments can be drawn in two steps of five each, as follows:
"""

def minimum_seconds_to_draw_segments(points):
    xt = yt = xl = xr = yl = yr = 0
    
    for x, y in points:
        if x == 0:
            yt += 1
            if y < 0:
                yl += 1
            if y > 0:
                yr += 1
        if y == 0:
            xt += 1
            if x < 0:
                xl += 1
            if x > 0:
                xr += 1
    
    ttx = (xt + 1) // 2 * (xt // 2)
    tty = (yt + 1) // 2 * (yt // 2)
    ii = xl * xr + yl * yr
    cc = min(max(xl, xr), max(yl, yr))
    
    return max(ttx, tty, ii, cc)