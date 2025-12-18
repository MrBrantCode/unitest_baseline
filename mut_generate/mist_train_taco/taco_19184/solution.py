"""
QUESTION:
Adam is standing at point $(a,b)$ in an infinite 2D grid. He wants to know if he can reach point $(x,y)$ or not. The only operation he can do is to move to point $(a+b,b),(a,a+b),(a-b,b),\text{or}(a,b-a)$ from some point $(a,b)$. It is given that he can move to any point on this 2D grid, i.e., the points having positive or negative $\mbox{X}$(or $\mathbf{Y}$) co-ordinates.  

Tell Adam whether he can reach $(x,y)$ or not.

Input Format

The first line contains an integer, $\mathbf{T}$, followed by $\mathbf{T}$ lines, each containing $4$ space-separated integers i.e. $\boldsymbol{a}$, $\boldsymbol{b}$, $\boldsymbol{x}$ and $y$.  

Constraints

$1\leq T\leq1000$  
$1\leq a,b,x,y\leq10^{18}$ 

Output Format

For each test case, display YES or NO that indicates if Adam can reach $(x,y)$ or not.  

Sample Input
3
1 1 2 3
2 1 2 3
3 3 1 1

Sample Output
YES
YES
NO

Explanation

(1,1) -> (2,1) -> (2,3).
"""

def can_reach(a: int, b: int, x: int, y: int) -> bool:
    """
    Determines if Adam can reach the point (x, y) from the point (a, b) on an infinite 2D grid.
    
    Adam can move to points (a+b, b), (a, a+b), (a-b, b), or (a, b-a).
    
    Parameters:
    a (int): The x-coordinate of the starting point.
    b (int): The y-coordinate of the starting point.
    x (int): The x-coordinate of the target point.
    y (int): The y-coordinate of the target point.
    
    Returns:
    bool: True if Adam can reach (x, y), False otherwise.
    """
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    return gcd(a, b) == gcd(x, y)