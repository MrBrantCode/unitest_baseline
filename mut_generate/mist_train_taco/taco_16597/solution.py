"""
QUESTION:
There is a square-shaped grid with N vertical rows and N horizontal columns. We will denote the square at the i-th row from the top and the j-th column from the left as (i,\ j).

Initially, each square is either white or black. The initial color of the grid is given to you as characters a_{ij}, arranged in a square shape. If the square (i,\ j) is white, a_{ij} is `.`. If it is black, a_{ij} is `#`.

You are developing a robot that repaints the grid. It can repeatedly perform the following operation:

* Select two integers i, j (1 ≤ i,\ j ≤ N). Memorize the colors of the squares (i,\ 1), (i,\ 2), ..., (i,\ N) as c_1, c_2, ..., c_N, respectively. Then, repaint the squares (1,\ j), (2,\ j), ..., (N,\ j) with the colors c_1, c_2, ..., c_N, respectively.



Your objective is to turn all the squares black. Determine whether it is possible, and find the minimum necessary number of operations to achieve it if the answer is positive.

Constraints

* 2 ≤ N ≤ 500
* a_{ij} is either `.` or `#`.

Input

The input is given from Standard Input in the following format:


N
a_{11}...a_{1N}
:
a_{N1}...a_{NN}


Output

If it is possible to turn all the squares black, print the minimum necessary number of operations to achieve the objective. If it is impossible, print `-1` instead.

Examples

Input

2
#.
.#


Output

3


Input

2
.
.#


Output

3


Input

2
..
..


Output

-1


Input

2


Output

0


Input

3
.#.

.#.


Output

2


Input

3
...
.#.
...


Output

5
"""

def min_operations_to_blacken_grid(n, grid):
    # Check if there is any black square in the grid
    for row in grid:
        if '#' in row:
            break
    else:
        return -1
    
    # Initialize variables
    ans = 10 ** 20
    black_cnt = [0] * n
    exist = [False] * n
    
    # Count black squares in each row and mark columns that contain black squares
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                black_cnt[i] += 1
                exist[j] = True
    
    # Count columns that are already fully black
    all_cnt = 0
    for j in range(n):
        for i in range(n):
            if grid[i][j] == '.':
                break
        else:
            all_cnt += 1
    
    # Calculate the minimum number of operations needed
    for i in range(n):
        if exist[i]:
            ans = min(ans, n - black_cnt[i] + n - all_cnt)
        else:
            ans = min(ans, 2 * n - black_cnt[i] - all_cnt + 1)
    
    return ans