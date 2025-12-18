"""
QUESTION:
A group of $n$ friends living in an $m$-dimensional hyperspace want to meet up at some central location. The hyperspace is in the form of an $m$-dimensional grid, and each person can only move along grid lines. For example, to go from $(0,0)\rightarrow(1,1)$ in a $2$-dimensional space, one possible route is $(0,0)\to(0,1)\to(1,1)$ for a total distance traveled of $2$ units.

Given the coordinates, $(X[0,1,\ldots,m-1])$, for $n$ friends, find a point at which all $n$ friends can meet such that the total sum of the distances traveled by all $n$ friends is minimal. If there are multiple such points, choose the lexicographically smallest one. The point $P_1[0,1,\ldots,m-1]$ is lexicographically smaller than $P_2[0,1,\ldots,m-1]$ if there exists such $j\lt m$ that $\forall i<j P_1[i]=P_2[i]$ and $P_1[j]<P_2[j]$.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $m$. 

Each line ${i}$ of the $n$ subsequent lines contains $m$ space-separated integers describing the respective coordinates (i.e., $x_0,x_1,\ldots,x_{m-1}$) for friend ${i}$.

Constraints

$1\leq n\leq10^4$  
$1\leq m\leq10^2$  
$-10^9\leq x_i\leq10^9$  

Output Format

Print $m$ space-separated integers describing the coordinates of the meeting point.

Sample Input
3 2
1 1
2 2
3 3

Sample Output
2 2

Explanation

There are $n=3$ friends (we'll call them ${a}$, ${b}$, and ${c}$) located at points $a=(1,1)$, $b=(2,2)$, and $c=(3,3)$. The minimal solution is for friends ${a}$ and ${c}$ to meet at friend ${b}$'s current location; this means ${a}$ travels $2$ units from $(1,1)$ to $(2,2)$, ${c}$ travels $2$ units from $(3,3)$ to $(2,2)$, and ${b}$ stays put at $(2,2)$. The total distance traveled by all friends is $2+0+2=4$, which is minimal. Thus, we print $m=2$ space-separated integers describing the coordinate where the $n=3$ friends meet: 2 2.
"""

import operator

def find_meeting_point(n, m, coordinates):
    # Transpose the coordinates to group by dimension
    coords = map(sorted, zip(*coordinates))
    # Get the median for each dimension
    getter = operator.itemgetter((n - 1) // 2)
    # Return the lexicographically smallest meeting point
    return list(map(getter, coords))