"""
QUESTION:
Two cats and a mouse are at various positions on a line.  You will be given their starting positions.  Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed.  If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given $\textit{q}$ queries in the form of $\boldsymbol{x}$, $y$, and $z$ representing the respective positions for cats $\mbox{A}$ and $\mbox{B}$, and for mouse $\mbox{C}$. Complete the function $catAndMouse$ to return the appropriate answer to each query, which will be printed on a new line.

If cat $\mbox{A}$ catches the mouse first, print Cat A.
If cat $\mbox{B}$ catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.  

Example  

$x=2$ 

$y=5$ 

$z=4$  

The cats are at positions $2$ (Cat A) and $5$ (Cat B), and the mouse is at position $4$.  Cat B, at position $5$ will arrive first since it is only $1$ unit away while the other is $2$ units away.  Return 'Cat B'.  

Function Description  

Complete the catAndMouse function in the editor below.  

catAndMouse has the following parameter(s):  

int x: Cat $\mbox{A}$'s position  
int y: Cat $\mbox{B}$'s position  
int z: Mouse $\mbox{C}$'s position  

Returns  

string:  Either 'Cat A', 'Cat B', or 'Mouse C'

Input Format

The first line contains a single integer, $\textit{q}$, denoting the number of queries. 

Each of the $\textit{q}$ subsequent lines contains three space-separated integers describing the respective values of $\boldsymbol{x}$ (cat $\mbox{A}$'s location), $y$ (cat $\mbox{B}$'s location), and $z$ (mouse $\mbox{C}$'s location).

Constraints

$1\leq q\leq100$  
$1\le x,y,z\le100$  

Sample Input 0
2
1 2 3
1 3 2

Sample Output 0
Cat B
Mouse C

Explanation 0

Query 0: The positions of the cats and mouse are shown below:

Cat $\mbox{B}$ will catch the mouse first, so we print Cat B on a new line.

Query 1: In this query, cats $\mbox{A}$ and $\mbox{B}$ reach mouse $\mbox{C}$ at the exact same time:

Because the mouse escapes, we print Mouse C on a new line.
"""

def cat_and_mouse(x: int, y: int, z: int) -> str:
    distance_cat_a = abs(x - z)
    distance_cat_b = abs(y - z)
    
    if distance_cat_a < distance_cat_b:
        return 'Cat A'
    elif distance_cat_a > distance_cat_b:
        return 'Cat B'
    else:
        return 'Mouse C'