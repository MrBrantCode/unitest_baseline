"""
QUESTION:
Krishnakant is standing at $(0,0)$ in the Cartesian plane. He wants to go to the point $(x,y)$ in the same plane using only horizontal and vertical moves of $1$ unit. There are many ways of doing this, and he is writing down all such ways. Each way comprises of few ${H}$ moves and few $V}$ moves. i.e. moves in horizontal and vertical direction respectively. For example, if Krishnakant wants to go to point $(2,2)$ from point $(0,0)$, ${HVHV}$ is one of the possible ways.   

Given the value of ${K}$, he wants to know lexicographically $K^{{th}}$ smallest way of going to $(x,y)$ from $(0,0)$.   

Input Format 

The first line contains an integer ${T}$ , i.e., number of test cases. 

Next ${T}$ lines will contain integers ${x}$,$y$ and ${K}$.  

Output Format 

For each test case, print lexicographically $K^{{th}}$ smallest path.  

Constraints 

$1\leq T\leq1000000$ 

$1\leq x\leq10$ 

$1\leq y\leq10$ 

$0\leq K<\text{number of paths}$ 

Sample Input  

2
2 2 2
2 2 3

Sample Output  

HVVH
VHHV

Explanation

All the paths of going to $(2,2)$ from $(0,0)$ in lexicographically increasing order:

$0.HHVV$

$1.HVHV$

$2.HVVH$

$3.VHHV$

$4.VHVH$

$5.VVHH$
"""

import math

def find_kth_lexicographic_path(x, y, k):
    def paths(n, m):
        if min(n, m) < 0:
            return 0
        return math.factorial(n + m) // math.factorial(n) // math.factorial(m)
    
    res = []
    current_x, current_y = 0, 0
    
    while (current_x, current_y) != (x, y):
        n = paths(x - current_x - 1, y - current_y)
        if current_x + 1 <= x and k < n:
            res.append('H')
            current_x += 1
        else:
            k -= n
            res.append('V')
            current_y += 1
    
    return ''.join(res)