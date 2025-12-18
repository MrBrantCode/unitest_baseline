"""
QUESTION:
Given integers ${b}$ and $a$, find the smallest integer ${h}$, such that there exists a triangle of height ${h}$, base ${b}$, having an area of at least $a$.

Example 

$b=4$ 

${a=6}$  

The minimum height ${h}$ is $3$.  One example is a triangle formed at points (0, 0), (4, 0), (2, 3).  

Function Description  

Complete the lowestTriangle function in the editor below.  

lowestTriangle has the following parameters:  

int b: the base of the triangle  
int a: the minimum area of the triangle  

Returns  

int:  the minimum integer height to form a triangle with an area of at least $a$ 

Input Format

There are two space-separated integers ${b}$ and $a$, on a single line.

Constraints

$1\leq b\leq10^{6}$
$1\leq a\leq10^{6}$

Sample Input 0
2 2

Sample Output 0
2

Explanation 0

The task is to find the smallest integer height of the triangle with base $2$ and area at least $2$. It turns out, that there are triangles with height $2$, base $2$ and area $2$, for example a triangle with corners in the following points: $(1,1),(3,1),(1,3)$:  

It can be proved that there is no triangle with integer height smaller than $2$, base $2$ and area at least $2$.

Sample Input 1
17 100

Sample Output 1
12

Explanation 1

The task is to find the smallest integer height of the triangle with base $17$ and area at least $100$.It turns out,that there are triangels with height $12$,base $17$ and area $102$ for example a triangle with corners in the following points: $(2,2),(19,2),(16,14)$. 

It can be proved that there is no triangle with integer height smaller than $12$, base $17$ and area at least $100$
"""

from math import ceil

def lowestTriangle(base, area):
    return ceil((2 * area) / base)