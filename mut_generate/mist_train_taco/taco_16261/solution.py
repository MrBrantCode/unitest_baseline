"""
QUESTION:
Draw a chessboard which has a height of H cm and a width of W cm. For example, the following figure shows a chessboard which has a height of 6 cm and a width of 10 cm.


.#.#.#.#.
.#.#.#.#.#
.#.#.#.#.
.#.#.#.#.#
.#.#.#.#.
.#.#.#.#.#


Note that the top left corner should be drawn by '#'.

Constraints

* 1 ≤ H ≤ 300
* 1 ≤ W ≤ 300

Input

The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output

For each dataset, print the chessboard made of '#' and '.'.

Print a blank line after each dataset.

Example

Input

3 4
5 6
3 3
2 2
1 1
0 0


Output

#.#.
.#.#
#.#.

#.#.#.
.#.#.#
#.#.#.
.#.#.#
#.#.#.

#.#
.#.
#.#

#.
.#

#
"""

def generate_chessboard(H: int, W: int) -> list[str]:
    if H == 0 and W == 0:
        return []
    
    chessboard = []
    for i in range(H):
        row = ''
        for j in range(W):
            row += '#' if (i + j) % 2 == 0 else '.'
        chessboard.append(row)
    
    return chessboard