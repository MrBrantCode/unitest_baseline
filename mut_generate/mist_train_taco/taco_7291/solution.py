"""
QUESTION:
An area named Renus, is divided into $(N \times M)$ cells. According to archaeological survey the area contains huge amount of treasure. Some cells out of $(N \times M)$ cells contain treasure. But problem is, you can't go to every cell as some of the cells are blocked.  
For every $a_{ij}$ cell($1 \leq i \leq N$,$1 \leq j \leq M$), your task is to find the distance of the nearest cell having treasure. 
Note:
- You can only traverse up, down, left and right from a given cell.
- Diagonal movements are not allowed.
- Cells having treasure can't be blocked, only empty cells ( cells without treasure) can be blocked.  

-----Input Format:------
- First line contains $T$, the number of test cases.
- Second line contains two space-separated integers $N\ and\ M$.
- Third line contains a single integer $X$ denoting number of cells having treasures, followed by $X$ lines containing two space-separated integers $x_i$ and $y_i$ denoting  position of row and column of $i^{th}$ treasure, for every $1\leq i \leq X$
- The next line contains a single integer $Y$ denoting the number of cells that are blocked, and it is followed by subsequent $Y$ lines containing  two space-separated integers $u_i$ and $v_i$ denoting position of row and column of blocked cells , for every $1\leq i \leq Y$

-----Constraints:------
- $1\le T \le 100$
- $1 \le N, M \le 200$
- $1 \le X < N*M$
- $0 \le Y <(N*M) - X$
- $1 \le x_i,u_j \le N, for\ every\ 1 \le i \le X\ and\ 1 \le j \le Y$
- $1 \le y_i,v_j \le M, for\ every\ 1 \le i \le X\ and\ 1 \le j \le Y$

-----Output Format:------
For each test case print a $N \times M$ matrix where each cell consists of distance of nearest treasure. Cells that are blocked will show "$X$" (without quotes). Also cells that doesn't have access to any treasure will show "$-1$" (without quotes).
Note: Co-ordinate of top left cell is $(1,1)$.

-----Sample Input-----
1
3 3
2
1 1
1 3
2
2 1
2 2

-----Sample Output-----
0 1 0 
X X 1
4 3 2

-----Explanation:-----
- Coordinates  (1,1) and (1,3)  shows "0" because they contain treasure and nearest distance is 0.
- Coordinates (2,1) and (2,2) shows "X" as they are blocked.
- Rest shows distance of nearest cell having treasure.
"""

def calculate_treasure_distances(N, M, treasures, blocked):
    # Initialize the matrix with large values
    mat = [[0] * (M + 2) for _ in range(N + 2)]
    ans = [[1000000000] * (M + 2) for _ in range(N + 2)]
    
    # Mark treasures
    for (x, y) in treasures:
        mat[x][y] = 1
        ans[x][y] = 0
    
    # Mark blocked cells
    for (u, v) in blocked:
        mat[u][v] = 1000000000
        ans[u][v] = 1000000000
    
    # Calculate distances
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if mat[i][j] == 1 or mat[i][j] == 1000000000:
                continue
            else:
                ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1, ans[i - 1][j] + 1)
    
    for i in range(N, 0, -1):
        for j in range(M, 0, -1):
            if mat[i][j] == 1 or mat[i][j] == 1000000000:
                continue
            else:
                ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1, ans[i][j + 1] + 1)
    
    for i in range(1, N + 1):
        for j in range(M, 0, -1):
            if mat[i][j] == 1 or mat[i][j] == 1000000000:
                continue
            else:
                ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1, ans[i][j + 1] + 1)
    
    for i in range(N, 0, -1):
        for j in range(1, M + 1):
            if mat[i][j] == 1 or mat[i][j] == 1000000000:
                continue
            else:
                ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1, ans[i][j - 1] + 1)
    
    # Prepare the result matrix
    result = []
    for i in range(1, N + 1):
        row = []
        for j in range(1, M + 1):
            if mat[i][j] == 1000000000:
                row.append('X')
            elif ans[i][j] >= 1000000000:
                row.append('-1')
            else:
                row.append(str(ans[i][j]))
        result.append(row)
    
    return result