"""
QUESTION:
Sean invented a game involving a $2n\times2n$ matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times.  The goal of the game is to maximize the sum of the elements in the $n\times n$ submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for $\textit{q}$ matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.  

Example 

$matrix=[[1,2],[3,4]]$  

1 2
3 4

It is $2\times2$ and we want to maximize the top left quadrant, a $1\times1$ matrix.  Reverse row $1$:

1 2
4 3

And now reverse column $0$:

4 2
1 3

The maximal sum is $4$.

Function Description  

Complete the flippingMatrix function in the editor below.  

flippingMatrix has the following parameters: 

- int matrix[2n][2n]: a 2-dimensional array of integers  

Returns 

- int: the maximum sum possible.   

Input Format

The first line contains an integer $\textit{q}$, the number of queries.   

The next $\textit{q}$ sets of lines are in the following format:

The first line of each query contains an integer, $n$. 
Each of the next $2n$ lines contains $2n$ space-separated integers $matrix[i][j]$ in row $\boldsymbol{i}$ of the matrix.  

Constraints

$1\leq q\leq16$  
$1\leq n\leq128$  
$0\leq matrix[i][j]\leq4096$, where $0\leq i,j<2n$.

Sample Input
STDIN           Function
-----           --------
1               q = 1
2               n = 2
112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
15 78 101 43
62 98 114 108

Sample Output
414

Explanation

Start out with the following $2n\times2n$ matrix:

$matrix=\begin{bmatrix}112&42&83&119\\ 56&125&56&49\\ 15&78&101&43\\ 62&98&114&108\end{bmatrix}$

Perform the following operations to maximize the sum of the $n\times n$ submatrix in the upper-left quadrant:

Reverse column $2$ ($[83,56,101,114]\rightarrow[114,101,56,83]$), resulting in the matrix: 

$matrix=\begin{bmatrix}112&42&114&119\\ 56&125&101&49\\ 15&78&56&43\\ 62&98&83&108\end{bmatrix}$

Reverse row $0$ ($[112,42,114,119]\rightarrow[119,114,42,112]$), resulting in the matrix: 

$matrix=\begin{bmatrix}119&114&42&112\\ 56&125&101&49\\ 15&78&56&43\\ 62&98&83&108\end{bmatrix}$

The sum of values in the $n\times n$ submatrix in the upper-left quadrant is $119+114+56+125=414$.
"""

def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0
    
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], 
                           matrix[2 * n - 1 - i][j], 
                           matrix[i][2 * n - 1 - j], 
                           matrix[2 * n - 1 - i][2 * n - 1 - j])
    
    return max_sum