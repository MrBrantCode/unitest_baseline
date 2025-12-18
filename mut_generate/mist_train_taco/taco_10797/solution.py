"""
QUESTION:
Mr K has a rectangular plot of land which may have marshes where fenceposts cannot be set. He wants you to find the perimeter of the largest rectangular fence that can be built on this land.

For example, in the following $m\times n=4\times4$ grid, $\boldsymbol{x}$ marks a marsh and $\boldsymbol{.}$ marks good land.

....
..x.
..x.
x...

If we number the rows and columns starting with $\mbox{1}$, we see that there are two main areas that can be fenced: $(1,1)-(3,2)$ and $(1,2)-(4,4)$.  The longest perimeter is $10$.  

Function Description

Complete the kMarsh function in the editor below.  It should print either an integer or impossible.

kMarsh has the following parameter(s):  

grid: an array of strings that represent the grid  

Input Format

The first line contains two space-separated integers $m$ and $n$, the grid rows and columns. 

Each of the next $m$ lines contains $n$ characters each describing the state of the land. 'x' (ascii value: 120) if it is a marsh and '.' ( ascii value:46) otherwise.  

Constraints

$2\leq m,n\leq500$ 

Output Format

Output contains a single integer - the largest perimeter. If the rectangular fence cannot be built, print impossible.

Sample Input 0

4 5
.....
.x.x.
.....
.....

Sample Output 0

14

Explanation 0  

The fence can be put up around the entire field. The perimeter is 
$2*(4-1)+2*(5-1)=14$.

Sample Input 1

2 2
.x
x.

Sample Output 1

impossible

Explanation 1

We need a minimum of 4 points to place the 4 corners of the fence. Hence, impossible. 

Sample Input 2

2 5
.....
xxxx.

Sample Output 2

impossible
"""

def calculate_largest_fence_perimeter(grid):
    m = len(grid)
    n = len(grid[0])
    
    # Convert grid to a 2D list of integers where 0 represents good land and 1 represents marsh
    land = [[0 if c == '.' else 1 for c in row] for row in grid]
    
    # Precompute the next free cell below for each cell
    next_free_below = [[-1] * n for _ in range(m)]
    for i in range(n):
        last_free = m - 1
        for j in range(m - 1, -1, -1):
            if land[j][i] == 1:
                last_free = j - 1
            else:
                next_free_below[j][i] = last_free
        next_free_below[m - 1][i] = -1
    
    # Precompute the next free cell to the right for each cell
    next_free_right = [[-1] * n for _ in range(m)]
    for i in range(m):
        last_free = n - 1
        for j in range(n - 1, -1, -1):
            if land[i][j] == 1:
                last_free = j - 1
            else:
                next_free_right[i][j] = last_free
        next_free_right[i][n - 1] = -1
    
    max_so_far = 0
    for i1 in range(m - 1):
        for j1 in range(n - 1):
            if land[i1][j1] == 1:
                continue
            for i2 in range(next_free_below[i1][j1], i1, -1):
                if 2 * (i2 - i1) + 2 * (next_free_right[i1][j1] - j1) < max_so_far:
                    continue
                for j2 in range(next_free_right[i1][j1], j1, -1):
                    if (land[i1][j1] == 0 and land[i2][j2] == 0 and 
                        next_free_below[i1][j1] >= i2 and 
                        next_free_right[i1][j1] >= j2 and 
                        next_free_below[i1][j2] >= i2 and 
                        next_free_right[i2][j1] >= j2):
                        max_so_far = max(max_so_far, 2 * (i2 - i1) + 2 * (j2 - j1))
    
    return max_so_far if max_so_far else 'impossible'