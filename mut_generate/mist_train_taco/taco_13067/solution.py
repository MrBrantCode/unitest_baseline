"""
QUESTION:
You are given an integer $n$. A set, $\mbox{S}$, of triples $(x_i,y_i,z_i)$ is beautiful if and only if:

$0\leq x_i,y_i,z_i$
$x_i+y_i+z_i=n,\forall i:1\leq i\leq|S|$
Let $\mbox{X}$ be the set of different $x_i$'s in $\mbox{S}$, $\mathbf{Y}$ be the set of different $y_i$'s in $\mbox{S}$, and $\mbox{Z}$ be the set of different $z_i$ in $\mbox{S}$. Then $|X|=|Y|=|Z|=|S|$.

The third condition means that all $x_i$'s are pairwise distinct. The same goes for $y_i$ and $z_i$.

Given $n$, find any beautiful set having a maximum number of elements. Then print the cardinality of $\mbox{S}$ (i.e., $\left|S\right|$) on a new line, followed by $\left|S\right|$ lines where each line contains $3$ space-separated integers describing the respective values of $x_i$, $y_i$, and $z_i$.

Input Format

A single integer, $n$.

Constraints

$1\leq n\leq300$  

Output Format

On the first line, print the cardinality of $\mbox{S}$ (i.e., $\left|S\right|$). 

For each of the $\left|S\right|$ subsequent lines, print three space-separated numbers per line describing the respective values of $x_i$, $y_i$, and $z_i$ for triple $\boldsymbol{i}$ in $\mbox{S}$.

Sample Input
3

Sample Output
3
0 1 2
2 0 1
1 2 0

Explanation

In this case, $n=3$. We need to construct a set, $\mbox{S}$, of non-negative integer triples ($x_{i},y_{i},z_{i}$) where $x_{i}+y_{i}+z_{i}=n$. $\mbox{S}$ has the following triples:

$(x_1,y_1,z_1)=(0,1,2)$
$(x_2,y_2,z_2)=(2,0,1)$
$(z_3,y_3,z_3)=(1,2,0)$

We then print the cardinality of this set, $|S|=3$, on a new line, followed by $3$ lines where each line contains three space-separated values describing a triple in $\mbox{S}$.
"""

def generate_beautiful_set(n):
    low = n // 3
    high = 2 * n // 3
    cardinality = high + 1
    beautiful_set = []
    
    for i in range(low + 1):
        beautiful_set.append((i, 2 * (low - i), n + i - 2 * low))
    
    for j in range(low + 1, high + 1):
        beautiful_set.append((j, 2 * (high - j) + 1, n + j - 1 - 2 * high))
    
    return cardinality, beautiful_set