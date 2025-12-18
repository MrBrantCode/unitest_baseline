"""
QUESTION:
Suppose we have a 2D grid $A$ of infinite width and height of $N$ units. Each row of the grid can be represented in the form of $111\ldots100\ldots \infty$ where the $1$s are repeated $x$ times, $x > 0$. Implying that the row starts with $x$ consecutive $1$-s followed by all $0$-s. 

Initially all cells are unmarked. Cell (i,j) refers to the i-th row, and j-th column. (1,1) refers to the bottom-left cell.

Now you do the following in each step.

Choose an unmarked cell having 1. Let it be (i, j).
while((i,j) lies in the grid boundaries && A[i][j] == 1){
	mark[i][j] = true; i--; j--;
}

How many minimum number of steps are required to mark all the cells containing $1$?

Note: The number of consecutive $1$-s at each height is given by the array $W$ where $W_{i}$ represents the same at $i^{th}$ row.

------ Input: ------
First line will contain $T$, number of testcases. Then the testcases follow. 
Each testcase contain $2$ lines of input.
First line will contain $N$, height of the grid (number of rows). 
Second line contains $N$ space separated integers where $i^{th}$ index represents number of consecutive $1$-s at the beginning of row $i$.

------ Output: ------
For each testcase, output in a single line answer to the problem.

------ Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{5}$
$1 ≤ W_{i} ≤ 10^{9}$

----- Sample Input 1 ------ 
3
3
1 1 1
3
5 3 2
3
4 2 5
----- Sample Output 1 ------ 
3
7
8
----- explanation 1 ------ 
TestCase 1: All the points need to be considered to cover all $1$-s.

TestCase 2: The optimal set of starting points is $\{(1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1)\}$.

![fig1]
"""

def calculate_min_steps(N, W):
    # Initialize the minimum and maximum values
    min_ = 0
    max_ = W[0]
    count = 0
    
    # Iterate over the rows starting from the second row
    for i in range(1, N):
        minv = -(i + 1)
        maxv = W[i] - (i + 1)
        
        # Update the count based on the current min and max values
        count += min(max_, minv) - min(min_, minv)
        count += max(max_, maxv) - max(min_, maxv)
        
        # Update the min and max values for the next iteration
        min_ = minv
        max_ = maxv
    
    # Add the final difference between max and min to the count
    count += (max_ - min_)
    
    return count