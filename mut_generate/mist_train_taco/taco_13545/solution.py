"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef has finished his freshman year in college. As a present, his parents gave him a new problem to solve:

Chef has to fill a K x K square grid of integers in a certain way. Let us say that such a grid is valid if:
Each cell contains an integer from 1 and K (inclusive). 
No integer appears twice in the same row or the same column.

Let F(K) be maximum possible distance between the center of the square and the closest cell that contains 1, among all possible squares with the side length K.

Here, we use the following notions:
The distance between cell (x, y) and (i, j) is equal to |x-i|+|y-j|. 
The center of a K x K square is cell ((K+1)/2, (K+1)/2) for odd K. 

------ Input ------ 

The first line of input contains a single integer T denoting the number of test cases.

Each test case consists of a single line containing a single odd integer K.

------ Output ------ 

For each test case, print K lines each consisting of K space separated integers giving some square grid where the distance from the center of the grid to the nearest 1 is exactly F(K). If there's more than 1 possible answer output any of them.

------ Constraints ------ 

$K_{i} is odd.$
Subtask #1 (10 points)  :
$ 1 ≤ T ≤ 50  $
$ 1 ≤ K_{i}≤ 5 $ 
Subtask #1 (90 points)  :
$ 1 ≤ T ≤ 10  $
$ 1 ≤ K_{i} < 400 $ 

----- Sample Input 1 ------ 
2
1
3
----- Sample Output 1 ------ 
1
3 2 1
1 3 2
2 1 3
"""

def generate_valid_grid(K):
    # Initialize the grid with zeros
    grid = [[0 for _ in range(K)] for _ in range(K)]
    
    # Calculate the center of the grid
    center = (K + 1) // 2
    
    # Place 1s in the grid according to the problem constraints
    for i in range(K // 2 + 1):
        grid[center - 1 + i][i] = 1
    for i in range(K // 2):
        grid[i][center + i] = 1
    
    # Fill the rest of the grid with appropriate values
    for i in range(K):
        e = grid[i].index(1)
        for j in range(1, K):
            grid[i][e - j] = j + 1
    
    return grid