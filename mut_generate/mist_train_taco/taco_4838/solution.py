"""
QUESTION:
Consider two points, $p=(p_x,p_y)$ and $q=(q_x,q_y)$. We consider the inversion or point reflection, $r=(r_x,r_y)$, of point ${p}$ across point ${q}$ to be a ${180^{\circ}}$ rotation of point ${p}$ around ${q}$.

Given $n$ sets of points ${p}$ and ${q}$, find ${r}$ for each pair of points and print two space-separated integers denoting the respective values of $r_{x}$ and $r_{y}$ on a new line.  

Function Description  

Complete the findPoint function in the editor below.  

findPoint has the following parameters:  

int px, py, qx, qy: x and y coordinates for points ${p}$ and $q}$  

Returns  

int[2]: x and y coordinates of the reflected point ${r}$  

Input Format

The first line contains an integer, $n$, denoting the number of sets of points. 

Each of the $n$ subsequent lines contains four space-separated integers that describe the respective values of $\boldsymbol{p_{x}}$, $p_y$, $q_{x}$, and $q_y$ defining points $p=(p_x,p_y)$ and $q=(q_x,q_y)$. 

Constraints

$1\leq n\leq15$  
$-100\leq p_x,p_y,q_x,q_y\leq100$  

Sample Input
2
0 0 1 1
1 1 2 2

Sample Output
2 2
3 3

Explanation

The graphs below depict points ${p}$, $q}$, and ${r}$ for the $n=2$ points given as Sample Input:
"""

def findPoint(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py
    return [rx, ry]