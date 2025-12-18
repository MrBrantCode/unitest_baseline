"""
QUESTION:
You are given an axis-aligned rectangle in a 2D Cartesian plane. The bottom left corner of this rectangle has coordinates (0,0)$(0, 0)$ and the top right corner has coordinates (N−1,N−1)$(N-1, N-1)$. You are also given K$K$ light sources; each light source is a point inside or on the perimeter of the rectangle.
For each light source, let's divide the plane into four quadrants by a horizontal and a vertical line passing through this light source. The light source can only illuminate one of these quadrants (including its border, i.e. the point containing the light source and two half-lines), but the quadrants illuminated by different light sources may be different.
You want to assign a quadrant to each light source in such a way that when they illuminate their respective quadrants, the entire rectangle (including its perimeter) is illuminated. Find out whether it is possible to assign quadrants to light sources in such a way.

-----Input-----
- The first line of the input contains an integer T$T$ denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains two space-separated integers K$K$ and N$N$.
- Each of the next K$K$ lines contains two space-separated integers x$x$ and y$y$ denoting a light source with coordinates (x,y)$(x, y)$.

-----Output-----
For each test case, print a single line containing the string "yes" if it is possible to illuminate the whole rectangle or "no" if it is impossible.

-----Constraints-----
- 1≤T≤5,000$1 \le T \le 5,000$
- 1≤K≤100$1 \le K \le 100$
- 1≤N≤109$1 \le N \le 10^9$
- 0≤x,y≤N−1$0 \le x, y \le N-1$
- no two light sources coincide

-----Example Input-----
2
2 10
0 0
1 0
2 10
1 2
1 1

-----Example Output-----
yes
no
"""

def can_illuminate_rectangle(K, N, points):
    if K > 3:
        return 'yes'
    
    sq = N - 1
    EWct = 0
    NSct = 0
    
    for (a, b) in points:
        EW = a == 0 or a == sq
        NS = b == 0 or b == sq
        if EW and NS:
            return 'yes'
        EWct += EW
        NSct += NS
    
    if NSct + EWct == 0 or len(points) == 1:
        return 'no'
    
    if EWct >= 2 or NSct >= 2:
        return 'yes'
    
    if len(points) == 2:
        return 'no'
    
    if NSct == 1 and EWct == 1:
        return 'yes'
    
    x = -1
    for (a, b) in points:
        if EWct > 0:
            if a == 0 or a == sq:
                e = b
            elif x == -1:
                x = b
            else:
                y = b
        elif b == 0 or b == sq:
            e = a
        elif x == -1:
            x = a
        else:
            y = a
    
    if (e - x) * (e - y) < 0:
        return 'no'
    else:
        return 'yes'