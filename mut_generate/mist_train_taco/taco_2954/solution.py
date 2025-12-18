"""
QUESTION:
Ema built a quantum computer! Help her test its capabilities by solving the problem below.

Given a grid of size $n\times m$, each cell in the grid is either $good$ or $\boldsymbol{bad}$.

A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment. 

In the diagram below, the blue pluses are valid and the orange ones are not valid.

Find the two largest valid pluses that can be drawn on $good$ cells in the grid, and return an integer denoting the maximum product of their areas.  In the above diagrams, our largest pluses have areas of $5$ and $\mbox{9}$.  The product of their areas is $5\times9=45$.

Note: The two pluses cannot overlap, and the product of their areas should be maximal.

Function Description  

Complete the twoPluses function in the editor below.  It should return an integer that represents the area of the two largest pluses.

twoPluses has the following parameter(s):  

grid: an array of strings where each string represents a row and each character of the string represents a column of that row  

Input Format

The first line contains two space-separated integers, $n$ and $m$. 

Each of the next $n$ lines contains a string of $m$ characters where each character is either G ($good$) or B ($\boldsymbol{bad}$). These strings represent the rows of the grid.  If the $y^{th}$ character in the $x^{th}$ line is G, then $(x,y)$ is a $good$ cell.  Otherwise it's a $\boldsymbol{bad}$ cell.

Constraints

$2\leq n\leq15$

$2\leq m\leq15$

Output Format

Find $2$ pluses that can be drawn on $good$ cells of the grid, and return an integer denoting the maximum product of their areas.

Sample Input 0

5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

Sample Output 0

5

Sample Input 1

6 6
BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB

Sample Output 1

25

Explanation

Here are two possible solutions for Sample 0 (left) and Sample 1 (right):

Explanation Key:

Green: $good$ cell
Red: $\boldsymbol{bad}$ cell
Blue: possible $pluses$. 

For the explanation below, we will refer to a plus of length $\boldsymbol{i}$ as $P_i$.

Sample 0 

There is enough good space to color one $P_3$ plus and one $\mathbf{P_1}$ plus. $Area(P_3)=5\:units$, and $Area(P_1)=1\:\textit{unit}$. The product of their areas is $5\times1=5$.

Sample 1 

There is enough good space to color two $P_3$ pluses. $Area(P_3)=5\:units$. The product of the areas of our two $P_3$ pluses is $5\times5=25$.
"""

def two_pluses_max_product(grid):
    def solve(y, x, y1, x1, l):
        i = 0
        s = True
        t = True
        ans = []
        while True:
            if s:
                a = l[y + i][x] if y + i < len(l) else 'B'
                b = l[y - i][x] if 0 <= y - i else 'B'
                c = l[y][x - i] if 0 <= x - i else 'B'
                d = l[y][x + i] if x + i < len(l[0]) else 'B'
                if a == b == c == d == 'G':
                    l[y + i][x] = 'B'
                    l[y - i][x] = 'B'
                    l[y][x - i] = 'B'
                    l[y][x + i] = 'B'
                else:
                    ans.append((i - 1) * 4 + 1)
                    s = False
            if t:
                e = l[y1 + i][x1] if y1 + i < len(l) else 'B'
                f = l[y1 - i][x1] if 0 <= y1 - i else 'B'
                g = l[y1][x1 - i] if 0 <= x1 - i else 'B'
                h = l[y1][x1 + i] if x1 + i < len(l[0]) else 'B'
                if e == f == g == h == 'G':
                    l[y1 + i][x1] = 'B'
                    l[y1 - i][x1] = 'B'
                    l[y1][x1 - i] = 'B'
                    l[y1][x1 + i] = 'B'
                else:
                    ans.append((i - 1) * 4 + 1)
                    t = False
            i += 1
            if not s and (not t):
                break
        return max(0, ans[0] * ans[1])

    l = [list(row) for row in grid]
    ans = 0
    for y in range(len(l)):
        for x in range(len(l[0])):
            for y1 in range(len(l)):
                for x1 in range(len(l[0])):
                    if l[y][x] == 'B' or l[y1][x1] == 'B':
                        continue
                    t = [row[:] for row in l]
                    ans = max(ans, solve(y, x, y1, x1, t))
    return ans