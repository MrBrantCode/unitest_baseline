"""
QUESTION:
You are standing at point $(0,0)$ on an infinite plane. In one step, you can move from some point $(x_f,y_f)$ to any point $(x_t,y_t)$ as long as the Euclidean distance, $\sqrt{(x_f-x_t)^2+(y_f-y_t)^2}$, between the two points is either $\boldsymbol{a}$ or $\boldsymbol{b}$. In other words, each step you take must be exactly $\boldsymbol{a}$ or $\boldsymbol{b}$ in length.

You are given $\textit{q}$ queries in the form of $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{d}$. For each query, print the minimum number of steps it takes to get from point $(0,0)$ to point $\left(d,0\right)$ on a new line.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries you must process. 

Each of the $\textit{q}$ subsequent lines contains three space-separated integers describing the respective values of $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{d}$ for a query. 

Constraints

$1\leq q\leq10^5$
$1\leq a<b\leq10^9$
$0\leq d\leq10^9$

Output Format

For each query, print the minimum number of steps necessary to get to point $\left(d,0\right)$ on a new line.

Sample Input 0
3
2 3 1
1 2 0
3 4 11

Sample Output 0
2
0
3

Explanation 0

We perform the following $q=3$ queries:

One optimal possible path requires two steps of length $\boldsymbol{a}=2$: $(0,0)\underset{2}{\longrightarrow}(\frac{1}{2},\frac{\sqrt{15}}{2})\underset{2}{\longrightarrow}(1,0)$. Thus, we print the number of steps, $2$, on a new line.
The starting and destination points are both $(0,0)$, so we needn't take any steps. Thus, we print $\mbox{0}$ on a new line.
One optimal possible path requires two steps of length $\boldsymbol{b}=4$ and one step of length $\boldsymbol{a}=3$: $(0,0)\underset{4}{\longrightarrow}(4,0)\underset{4}{\longrightarrow}(8,0)\underset{3}{\longrightarrow}(11,0)$. Thus, we print $3$ on a new line.
"""

from math import ceil

def minimum_steps_to_reach(a, b, d):
    mmin = min(a, b)
    mmax = max(a, b)
    
    if d == 0:
        return 0
    if d in {mmin, mmax}:
        return 1
    if d < mmax:
        return 2
    return ceil(d / mmax)