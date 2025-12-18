"""
QUESTION:
Let $length(A)$ denote the count of digits of a number $\mbox{A}$ in its decimal representation. 

John is looking for new methods of determining which numbers are strange all day long. 

All non-negative numbers of length 1 are strange. Further, a number $\mbox{X}$ with $length(X)\geq1$ can also be considered strange if and only if  

$\mbox{X}$ is evenly divisible by $length(X)$  
the number $X/length(X)$ is recursively strange

Your task is to calculate how many strange numbers belong to an interval $[L,R]$.  

Input Format 

The first line contains single integer $\mathbf{T}$ - the number of test cases. Next $\mathbf{T}$ lines contain two integers separated by single space $\boldsymbol{\mbox{L}}$ and $\mbox{R}$.  

Output Format 

In $\mathbf{T}$ lines, print $\mathbf{T}$ integers - count of strange numbers belonging to the interval $[L,R]$.

Constraints 

$1\leq T\leq200$ 

$0\leq L<R\leq10^{18}$  

Sample Input

5
7 25
45 50
1 100
99 103
0 1000000

Sample Output

10
1
26
0
96

Explanation 

First testcase: There are $10$ strange numbers that belong to the interval $[7,25]$. They are $7,8,9,10,12,14,16,18,20,24$. 

Second testcase: Only $48$ satisfies the given constraints.
"""

import math
import bisect

# Precompute the list of strange numbers
_l = [n for n in range(10)]
for i in range(2, 19):
    j = 1
    while j < len(_l):
        if i == int(math.log10(_l[j] * i)) + 1:
            _l.append(_l[j] * i)
        j += 1

# Helper function to find the number of strange numbers up to a given number
def s(n):
    return bisect.bisect(_l, n)

# Main function to count strange numbers in the interval [L, R]
def count_strange_numbers(L, R):
    if L == 0:
        return s(R)
    else:
        return s(R) - s(L - 1)