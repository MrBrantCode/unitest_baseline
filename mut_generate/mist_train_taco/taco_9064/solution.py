"""
QUESTION:
Let's solve the puzzle by programming.

The numbers n x n are arranged in a grid pattern. Some of the numbers are circled and we will call them the starting point. The rules of the puzzle are as follows:

* Draw one line that goes vertically and horizontally from each starting point (cannot be drawn diagonally).
* Extend the line so that the sum of the numbers passed is the same as the starting number.
* The line must not be branched.
* Lines cannot pass through numbers already drawn (lines must not intersect).
* A line cannot pass through more than one origin.



As shown in the figure below, the goal of the puzzle is to use all the starting points and draw lines on all the numbers.


<image>


Your job is to create a puzzle-solving program. However, in this problem, it is only necessary to determine whether the given puzzle can be solved.



Input

The input consists of multiple datasets. The format of each dataset is as follows:


n
n x n numbers


Indicates a puzzle given a number of n x n, the starting number is given as a negative number.

When n is 0, it indicates the end of input.

It can be assumed that n is 3 or more and 8 or less, numbers other than the starting point are 1 or more and 50 or less, and the starting point is -50 or more and -1 or less. You may also assume the following as the nature of the puzzle being entered:

* Each row and column of a given puzzle has at least one starting point.
* The number of starting points is about 20% to 40% of the total number of numbers (n x n).

Output

For each dataset, print "YES" if the puzzle can be solved, otherwise "NO" on one line.

Example

Input

3
-3 1 1
2 -4 1
2 1 -1
3
-4 1 1
1 1 -6
1 -5 3
4
-8 6 -2 1
2 -7 -2 1
1 -1 1 1
1 1 1 -5
6
2 2 3 -7 3 2
1 -10 1 1 3 2
2 6 5 2 -6 1
3 4 -23 2 2 5
3 3 -6 2 3 7
-7 2 3 2 -5 -13
6
2 2 3 -7 3 2
1 -10 1 1 3 2
2 6 5 2 -6 1
3 4 -23 2 2 5
3 3 -6 2 3 7
-7 2 3 2 -5 -12
0


Output

YES
NO
NO
YES
NO
"""

def can_solve_puzzle(n, grid):
    used = [[False] * n for _ in range(n)]
    inits = []
    
    for y in range(n):
        for x in range(n):
            if grid[y][x] < 0:
                inits.append((x, y, grid[y][x]))
                used[y][x] = True
    
    vec = ((0, 1), (-1, 0), (0, -1), (1, 0))
    
    def search(x, y, s, index, inits, end):
        if s == 0 and index == end:
            return True
        elif s == 0:
            (x, y, s) = inits[index]
            index += 1
        ret = False
        for (dx, dy) in vec:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n and (not used[ny][nx]) and (grid[ny][nx] + s <= 0):
                used[ny][nx] = True
                ret = ret or search(nx, ny, s + grid[ny][nx], index, inits, end)
                used[ny][nx] = False
        return ret
    
    if sum([sum(lst) for lst in grid]) != 0:
        return False
    elif search(0, 0, 0, 0, inits, len(inits)):
        return True
    else:
        return False