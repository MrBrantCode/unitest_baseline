"""
QUESTION:
You are given a straight line, $a\cdot x+b\cdot y=c$. Find the point closest to the origin that also satisfies the following properties:  

$\boldsymbol{x}$ and $y$ are integers.  
$\boldsymbol{x}$ is greater than zero.  

If more than one solution exists satisfying $\mbox{1}$ and $2$, then choose the point in which $\boldsymbol{x}$ is minimal.  

Given $\textit{q}$ queries consisting of $a_i$, $b_i$, and $c_i$, find and print the point satisfying the above conditions for each respective query. Each point must be printed on a new line as two space-separated integers denoting the point's respective $x_i$ and $y_i$ values.

Note: It is guaranteed that there will always be integral points on the line.  

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. 

Each line $\boldsymbol{i}$ of the $\textit{q}$ subsequent lines contains three space-separated integers describing the respective values of $a_i$, $b_i$, and $c_i$ for the query.  

Constraints

$1\leq q\leq10^5$  
$1\leq a\leq10^8$  
$1\leq b\leq10^8$  
$1\leq c\leq10^8$  

Output Format

For each query, print $2$ space-separated integers on a new line denoting the respective values of $x_i$ and $y_i$ for the point satisfying the $i^{\mbox{th}}$ query.

Sample Input
1
2 3 1

Sample Output
2 -1

Explanation

Given the line $2\cdot x+3\cdot y=1$, the point $(2,-1)$ is on the line and satisfies the conditions specified above. Thus, we print the coordinate as two space-separated integers on a new line.
"""

from math import floor

def GCD(a, b):
    if a < b:
        a, b = b, a
    while True:
        if a % b == 0:
            return b
        a, b = b, a % b

def GCDEx(a, b):
    if b == 0:
        return (1, 0)
    sx, sy = GCDEx(b, a % b)
    return (sy, sx - a // b * sy)

def closest(t):
    if abs(t - floor(t)) > 0.5:
        return floor(t) + 1
    else:
        return floor(t)

def find_closest_point(a, b, c):
    gcd = GCD(a, b)
    a //= gcd
    b //= gcd
    c //= gcd
    sx, sy = GCDEx(a, b)
    t1 = floor(-sx * c / b) + 1
    t2 = c * (a * sy - b * sx) / (a * a + b * b)
    if t1 >= t2:
        t = t1
    else:
        t = closest(t2)
    return (sx * c + t * b, sy * c - t * a)