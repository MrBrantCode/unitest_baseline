"""
QUESTION:
Watson gives Sherlock two integers, $n$ and $\boldsymbol{\mbox{k}}$, and asks him to count the number of positive integer $\boldsymbol{i}$'s such that: 

$i\cdot(n-i)\leq n\cdot k,\ \text{and}\ i<n$  

Given $\textit{q}$ queries where each query consists of some $n$ and $\boldsymbol{\mbox{k}}$, print the number of possible $\boldsymbol{i}$'s for each query on a new line.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of times Watson queries Sherlock. 

Each of the $\textit{q}$ subsequent lines contains two space-separated integers denoting the respective values of $n$ and $\boldsymbol{\mbox{k}}$ for a query.

Constraints

$1\leq q\leq10^5$   
$1\leq n,k\leq10^9$

Output Format

For each query, print the number of $\boldsymbol{i}$'s satisfying the given formula on a new line.

Sample Input
2
5 1
5 2

Sample Output
2
4

Explanation

Sherlock performs the following $q=2$ queries:

The possible values of $\boldsymbol{i}$ satisfying Watson's formula for $n=5$ and $k=1$ are $\mbox{1}$ and $\begin{array}{c}4\end{array}$. Because there are two such values, we print $2$ on a new line.
The possible values of $\boldsymbol{i}$ satisfying Watson's formula for $n=5$ and $k=2$ are $\mbox{I}$, $2$, $3$, and $\begin{array}{c}4\end{array}$. Because there are four such values, we print $\begin{array}{c}4\end{array}$ on a new line.
"""

def count_valid_i(n, k):
    if n * n - 4 * n * k < 0:
        return n - 1
    else:
        z1 = (n + (n * n - 4 * n * k) ** 0.5) / 2
        z2 = (n - (n * n - 4 * n * k) ** 0.5) / 2
        u = min(n, int(ceil(z1)))
        l = max(0, int(z2))
        return min(n - 1, l + n - u)