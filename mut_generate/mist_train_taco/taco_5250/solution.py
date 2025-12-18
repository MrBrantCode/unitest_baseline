"""
QUESTION:
Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board $\mbox{A}$ of size $H\times W$ with $\mbox{H}$ rows and $\mbox{W}$ columns. The board is divided into cells of size $1\times1$ with each cell indicated by its coordinate $(i,j)$. The cell $(i,j)$  has an integer $A_{ij}$ written on it. To create the toy Mason stacks $A_{ij}$ number of cubes of size $1\times1\times1$ on the cell $(i,j)$. 

Given the description of the board showing the values of $A_{ij}$ and that the price of the toy is equal to the 3d surface area find the price of the toy. 

Input Format

The first line contains two space-separated integers $\mbox{H}$ and $\mbox{W}$ the height and the width of the board respectively.

The next  $\mbox{H}$ lines contains $\mbox{W}$ space separated integers. The $j^{th}$ integer in $i^{\mbox{th}}$ line denotes $A_{ij}$.

Constraints

$1\leq H,W\leq100$
$1\le A_{i,j}\le100$

Output Format

Print the required answer, i.e the price of the toy, in one line.

Sample Input 0
1 1
1

Sample Output 0
6

Explanation 0

The surface area of $1\times1\times1$ cube is 6.

Sample Input 1
3 3
1 3 4
2 2 3
1 2 4

Sample Output 1
60

Explanation 1

The object is rotated so the front row matches column 1 of the input, heights 1, 2, and 1.  

The front face is 1 + 2 + 1 = 4 units in area.   
The top is 3 units.
The sides are 4 units.   
None of the rear faces are exposed.  
The underside is 3 units.  

The front row contributes 4 + 3 + 4 + 3 = 14 units to the surface area.
"""

def calculate_toy_price(H, W, A):
    def surface_area(A):
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx = j + dx
                    ny = i + dy
                    if 0 <= nx < len(A[0]) and 0 <= ny < len(A):
                        if nx >= j and ny >= i:
                            ans += abs(A[i][j] - A[ny][nx])
                    else:
                        ans += A[i][j]
        return ans

    # Calculate the surface area of the toy
    surface_area_result = surface_area(A)
    
    # Add the top and bottom surface areas
    total_surface_area = surface_area_result + H * W + H * W
    
    return total_surface_area