"""
QUESTION:
You will be given a square chess board with one queen and a number of obstacles placed on it.  Determine how many squares the queen can attack.  

A queen is standing on an $n\times n$ chessboard. The chess board's rows are numbered from $\mbox{I}$ to $n$, going from bottom to top.  Its columns are numbered from $\mbox{I}$ to $n$, going from left to right. Each square is referenced by a tuple, $(r,c)$, describing the row, $\textbf{r}$, and column, $\textbf{C}$, where the square is located.

The queen is standing at position $(r_q,c_q)$.  In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from $(4,4)$: 

There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location $(3,5)$ in the diagram above prevents the queen from attacking cells $(3,5)$, $(2,6)$, and $(1,7)$:

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at $(r_q,c_q)$.  In the board above, there are $24$ such squares.

Function Description  

Complete the queensAttack function in the editor below.   

queensAttack has the following parameters: 

- int n: the number of rows and columns in the board 

- nt k: the number of obstacles on the board 

- int r_q: the row number of the queen's position 

- int c_q: the column number of the queen's position 

- int obstacles[k][2]: each element is an array of $2$ integers, the row and column of an obstacle  

Returns 

- int: the number of squares the queen can attack   

Input Format

The first line contains two space-separated integers $n$ and $\boldsymbol{\mbox{k}}$, the length of the board's sides and the number of obstacles. 

The next line contains two space-separated integers $r_q$ and $c_{q}$, the queen's row and column position. 

Each of the next $\boldsymbol{\mbox{k}}$ lines contains two space-separated integers $r[i]$ and $c[i]$, the row and column position of $obstacle[i]$.       

Constraints

$0<n\leq10^5$
$0\leq k\leq10^5$
A single cell may contain more than one obstacle.
There will never be an obstacle at the position where the queen is located.

Subtasks

For $30\%$ of the maximum score: 

$0<n\leq100$
$0\leq k\leq100$

For $55\%$ of the maximum score: 

$0<n\leq1000$
$0\leq k\leq10^5$

Sample Input 0
4 0
4 4

Sample Output 0
9

Explanation 0

The queen is standing at position $(4,4)$ on a $4\times4$ chessboard with no obstacles:

Sample Input 1
5 3
4 3
5 5
4 2
2 3

Sample Output 1
10

Explanation 1

The queen is standing at position $(4,3)$ on a $5\times5$ chessboard with $k=3$ obstacles:

The number of squares she can attack from that position is $10$.

Sample Input 2
1 0
1 1

Sample Output 2
0

Explanation 2

Since there is only one square, and the queen is on it, the queen can move 0 squares.
"""

def queens_attack(n, k, r_q, c_q, obstacles):
    obstacles = set(obstacles)  # Convert obstacles list to a set for O(1) lookup
    ans = 0
    
    # Directions: (row_increment, col_increment)
    directions = [
        (0, -1),  # Left
        (0, 1),   # Right
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, -1), # Up-Left
        (-1, 1)   # Up-Right
    ]
    
    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n:
            if (r, c) in obstacles:
                break
            ans += 1
            r += dr
            c += dc
    
    return ans