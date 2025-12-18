"""
QUESTION:
It has been decided that a programming contest sponsored by company A will be held, so we will post the notice on a bulletin board.

The bulletin board is in the form of a grid with N rows and N columns, and the notice will occupy a rectangular region with H rows and W columns.

How many ways are there to choose where to put the notice so that it completely covers exactly HW squares?

Constraints

* 1 \leq H, W \leq N \leq 100
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
H
W


Output

Print the answer.

Examples

Input

3
2
3


Output

2


Input

100
1
1


Output

10000


Input

5
4
2


Output

8
"""

def count_notice_placements(N, H, W):
    if H > N or W > N:
        return 0
    else:
        return (N - W + 1) * (N - H + 1)