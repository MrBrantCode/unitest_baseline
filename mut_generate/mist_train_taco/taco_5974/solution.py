"""
QUESTION:
Given a matrix (H × W) which contains only 1 and 0, find the area of the largest square matrix which only contains 0s.

Constraints

* 1 ≤ H, W ≤ 1,400

Input


H W
c1,1 c1,2 ... c1,W
c2,1 c2,2 ... c2,W
:
cH,1 cH,2 ... cH,W


In the first line, two integers H and W separated by a space character are given. In the following H lines, ci,j, elements of the H × W matrix, are given.

Output

Print the area (the number of 0s) of the largest square.

Example

Input

4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0


Output

4
"""

def largest_square_of_zeros(grid):
    h = len(grid)
    w = len(grid[0])
    
    # Initialize a DP table with the same dimensions as the grid
    dp = [[0] * w for _ in range(h)]
    
    # Initialize the maximum length of the square found so far
    max_length = 0
    
    # Fill the DP table and update max_length
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0:
                # For the first row and first column, the value is either 0 or 1
                dp[i][j] = (grid[i][j] + 1) % 2
            else:
                if grid[i][j] == 0:
                    # If the current cell is 0, calculate the size of the square ending here
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                else:
                    # If the current cell is 1, the square ending here is of size 0
                    dp[i][j] = 0
            
            # Update the maximum length found so far
            max_length = max(max_length, dp[i][j])
    
    # The area of the largest square is the square of the side length
    return max_length ** 2