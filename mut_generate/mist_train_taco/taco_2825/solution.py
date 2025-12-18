"""
QUESTION:
Tetris is a game in which falling blocks are lined up on the board and erased. Here, let's consider a game that arranges it a little.

The size of the board of this game is 5 frames wide, and it is high enough to accommodate all the blocks that appear. The falling blocks are straight and come in two types, landscape and portrait, with five lengths from 1 to 5.

An example is shown below. The figure from Step (a) to Step (e) shows how the blocks fall and disappear. From Step (a), proceed in order of Step (b) and Step (c).

When dropping a block, if somewhere in the block is caught in a block piled up like Step (a), the dropped block like Step (b) will stop at that place. Also, as a result of dropping a block, if all the frames in a horizontal line on the board are clogged with blocks, the blocks in that line will disappear as shown in Step (d). After this, the block above the disappeared line will move down one line as it is (Step (e)).

<image>



In one game, up to 1000 blocks will be dropped in order. For example, the lengths of the falling blocks are 4 frames horizontally, 3 frames horizontally, 2 frames vertically, and 3 frames vertically, and the falling locations are the 1st, 1st, 4th, and 5th frames from the left end. If there is, it will drop as shown in Step (a) to (g) in the figure below, and the last remaining block will be 2 frames.

<image>



Create a program that inputs the information of the blocks that fall in order and outputs the number of frames remaining when all the blocks fall.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


n
d1 p1 q1
d2 p2 q2
::
dn pn qn


The number of blocks n (1 ≤ n ≤ 1000) is given on the first line. The next n lines give the i-th block orientation di (1 or 2), the block length pi (1 ≤ pi ≤ 5), and the block position qi. Block orientation di is 1 for landscape orientation and 2 for portrait orientation. The block position qi is an integer from 1 to 5 from the left edge on the board, and in the case of a horizontal block, it is the position where the left edge frame falls.

The number of datasets does not exceed 20.

Output

The number of frames occupied by the last remaining block for each data set is output on one line.

Example

Input

4
1 4 1
1 3 1
2 2 4
2 3 5
1
1 5 1
7
2 2 2
1 4 1
2 1 3
1 4 1
1 1 1
2 5 5
1 4 2
0


Output

2
0
6
"""

def calculate_remaining_frames(n, blocks):
    L = 5000
    MP = [[0] * L for _ in range(5)]
    cs = [L] * 5
    us = []
    U = [0] * L
    
    for i in range(n):
        d, p, q = blocks[i]
        q -= 1
        if d == 1:
            y = L
            for j in range(p):
                y = min(y, cs[q + j])
            y -= 1
            for j in range(p):
                MP[q + j][y] = 1
                cs[q + j] = y
            if all((MP[j][y] for j in range(5))):
                us.append(y)
        else:
            y = cs[q] - p
            for j in range(p):
                MP[q][y + j] = 1
            cs[q] = y
            for j in range(p):
                if all((MP[k][y + j] for k in range(5))):
                    us.append(y + j)
        if us:
            y0 = us[-1]
            for y in us:
                U[y] = 1
            for j in range(5):
                cur = y0
                for k in range(y0, cs[j] - 1, -1):
                    if U[k]:
                        continue
                    MP[j][cur] = MP[j][k]
                    cur -= 1
                for k in range(cur, cs[j] - 1, -1):
                    MP[j][k] = 0
                while cur < L and MP[j][cur] == 0:
                    cur += 1
                cs[j] = cur
            for y in us:
                U[y] = 0
            us = []
    
    ans = 0
    for j in range(5):
        for k in range(cs[j], L):
            ans += MP[j][k]
    
    return ans