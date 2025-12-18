"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Vietnamese], and [Bengali] as well.

You are given a grid with $N$ rows and $M$ columns, where each cell contains either '0' or '1'. 

Find out whether all the cells containing '1'-s form a rectangle, I.e, is there a rectangular contiguous subgrid such that every cell within it is a '1', and all the cells containing '1'-s are within this subgrid.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $M$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains a single string with length $M$ describing the $i$-th row of the grid.

------  Output ------
For each test case, print a single line containing the string "YES" if the connected component of '1'-s is a rectangle or "NO" if it is not.

Note: The output is case-insensitive ― each letter may be printed in upper case or lower case.

------  Constraints  ------
$1 ≤ T ≤ 1000$
$1 ≤ N, M ≤ 500$
Sum of $N*M$ over all tests is atmost $1.5*10^{6}$
Each string contains only characters '0' and '1'
It is guaranteed that grid contains at least a single '1'

----- Sample Input 1 ------ 
3
3 3
010
111
010
4 4
0000
0110
1110
1100
3 3
011
011
000
----- Sample Output 1 ------ 
NO
NO
YES
----- explanation 1 ------ 
Example case 1: The minimal rectangle which covers all '1'-s also covers $4$ cells which contain '0'-s.

Example case 2: The minimal rectangle which covers all '1'-s also covers $2$ cells which contain '0'-s.

Example case 3: We can form a minimal rectangle with side length $2$ which covers all cells containing '1'-s and none of the cells containing '0'-s.
"""

def is_rectangle_of_ones(test_cases):
    results = []
    
    for case in test_cases:
        N, M, grid = case
        min_row, max_row = N, -1
        min_col, max_col = M, -1
        
        # Find the bounding box of '1's
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j
        
        # Check if all '1's are within the bounding box
        is_rectangle = True
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if grid[i][j] != '1':
                    is_rectangle = False
                    break
            if not is_rectangle:
                break
        
        results.append("YES" if is_rectangle else "NO")
    
    return results