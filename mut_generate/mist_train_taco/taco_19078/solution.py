"""
QUESTION:
Chef has a grid of size N \times M. 

In one move, Chef can move from his current cell to an adjacent cell. If the Chef is currently at (i, j) then, in one move, Chef can move to (i + 1, j), (i - 1, j), (i, j + 1) or (i, j - 1).

There are also K *special* cells in the grid. These special cells support a corner move as well. If the Chef is currently at a *special* cell (i, j) then, in one move, Chef can move to (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1) or (i - 1, j + 1) in addition to the adjacent cells ((i + 1, j), (i - 1, j), (i, j + 1) or (i, j - 1)). 

Chef is not allowed to leave the grid at any moment. Determine the minimum number of moves Chef needs to go from (1, 1) to (N, M).

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains three space-separated integers N, M and K — the number of rows in the grid, the number of columns in the grid and the number of special cells.
- K lines follow. The i-th line of these K lines contains two space-separated integers X_{i} and Y_{i} such that (X_{i}, Y_{i}) is the i-th special cell.

------ Output Format ------ 

For each test case, output the minimum number of moves required by the Chef to go to (N, M) from (1, 1).

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$ 
$1 ≤ N, M ≤ 10^{9}$ 
$0 ≤ K ≤ 2 \cdot 10^{5}$ 
$1 ≤ X_{i} ≤ N$, $1 ≤ Y_{i} ≤ M$ 
- All $(X_{i}, Y_{i})$ are pairwise distinct.
- Sum of $K$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
3 3 0
3 3 2
2 2
2 3

----- Sample Output 1 ------ 
4
3

----- explanation 1 ------ 
Test Case 1: There is no special cell in this case. One of the optimal ways is: $(1,1) \rightarrow (1,2) \rightarrow (1,3) \rightarrow (2,3) \rightarrow (3,3)$. Therefore a total of $4$ moves is required.

Test Case 2: There are $2$ special cells in this case. One of the optimal ways is: $(1,1) \rightarrow (2,1) \rightarrow (2,2) \rightarrow (3,3)$. Therefore a total of $3$ moves is required.
"""

import bisect

def min_moves_to_reach_end(n, m, k, special_cells):
    def longest_incr_length(s):
        vec_last = []
        for x in s:
            i = bisect.bisect_left(vec_last, x)
            if i != len(vec_last):
                vec_last[i] = x
            else:
                vec_last.append(x)
        return len(vec_last)
    
    # Filter out special cells that are not useful
    specials = [(sx, sy) for (sx, sy) in special_cells if sx != n and sy != m]
    
    # Sort the special cells based on their coordinates
    specials.sort(key=lambda p: (p[0], -p[1]))
    
    # Calculate the longest increasing subsequence of y-coordinates
    max_spec = longest_incr_length([y for (x, y) in specials])
    
    # Calculate the minimum number of moves
    return m + n - 2 - max_spec