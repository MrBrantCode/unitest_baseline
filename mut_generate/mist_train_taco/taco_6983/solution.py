"""
QUESTION:
We have a board with an H \times W grid.
Each square in the grid is painted in black or white. The square at the i-th row from the top and j-th column from the left is black if the j-th character in S_i is #, and white if that character is ..
Snuke can perform the following operation on the grid any number of times:
 - Select a row or column in the grid, and invert the color of all the squares in that row or column (that is, black squares become white and vice versa).
Then, Snuke draws a rectangle along grid lines. Here, all the squares contained in the rectangle must be painted in black.
Find the maximum possible area of Snuke's rectangle when the operation is performed optimally.

-----Constraints-----
 - 2 \leq H \leq 2000
 - 2 \leq W \leq 2000
 - |S_i| = W
 - S_i consists of # and ..

-----Input-----
Input is given from Standard Input in the following format:
H W
S_1
S_2
:
S_H

-----Output-----
Print the maximum possible area of Snuke's rectangle.

-----Sample Input-----
3 3
..#
##.
.#.

-----Sample Output-----
6

If the first row from the top and the third column from the left are inverted, a 2 \times 3 rectangle can be drawn, as shown below:
"""

def max_black_rectangle_area(H, W, S):
    ans = max(H, W)
    T = [[0] * (W - 1)]
    
    for i in range(H - 1):
        t, ts = [], []
        for j in range(W - 1):
            r = S[i][j:j + 2] + S[i + 1][j:j + 2]
            t.append(r.count('.') % 2)
            if t[j] == 0:
                ts.append(T[-1][j] + 1)
            else:
                ts.append(0)
        T.append(ts)
    
    for L in T[1:]:
        stack = []
        for i, l in enumerate(L + [0]):
            w = -1
            while stack and stack[-1][1] >= l:
                w, h = stack.pop()
                ans = max(ans, (h + 1) * (i - w + 1))
            if w != -1:
                stack.append((w, l))
                continue
            stack.append((i, l))
    
    return ans