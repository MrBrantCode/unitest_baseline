"""
QUESTION:
Sherlock is given $2$ square tiles, initially both of whose sides have length $\boldsymbol{l}$ placed in an $x-y$ plane.  Initially, the bottom left corners of each square are at the origin and their sides are parallel to the axes.  

At $t=0$, both squares start moving along line $y=x$ (along the positive $\boldsymbol{x}$ and $y$) with velocities $\mbox{s1}$ and $\mbox{s2}$.     

For each querydetermine the time at which the overlapping area of tiles is equal to the query value, $\textit{queries}[i]$.  

Note: Assume all distances are in meters, time in seconds and velocities in meters per second.  

Function Description  

Complete the movingTiles function in the editor below.  

movingTiles has the following parameter(s):  

int l: side length for the two squares  
int s1: velocity of square 1
int s2: velocity of square 2
int queries[q]: the array of queries  

Returns  

int[n]: an array of answers to the queries, in order. Each answer will be considered correct if it is at most $\textbf{0.0001}$ away from the true answer.

Input Format 

First line contains integers $l,s1,s2$. 

The next line contains $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines consists of one integer $\textit{queries}[i]$ in one line.

Constraints 

$1\leq l,s1,s2\leq10^9$ 

$1\leq q\leq10^5$ 

$1\leq\textit{queries}[i]\leq L^2$ 

$s1\neq s2$  

Sample Input  

10 1 2
2
50
100

Sample Output  

4.1421
0.0000

Explanation  

For the first case, note that the answer is around 4.1421356237..., so any of the following will be accepted:  

4.1421356237
4.14214
4.14215000
4.1421
4.1422
"""

from math import sqrt

def moving_tiles(l, s1, s2, queries):
    results = []
    for query in queries:
        v = abs(sqrt(2) * (l - sqrt(query)) / (s2 - s1))
        results.append(round(v, 5))
    return results