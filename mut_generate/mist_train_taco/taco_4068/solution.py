"""
QUESTION:
Seen from above, there is a grid-like square shaped like Figure 1. The presence or absence of "walls" on each side of this grid is represented by a sequence of 0s and 1s. Create a program that stands at point A, puts your right hand on the wall, keeps walking in the direction of the arrow, and outputs the route to return to point A again.

<image>
---
Figure 1
---




Input

The input consists of 9 lines and is given in the following format, with 1 being the presence of a wall and 0 being the absence of a wall, as shown in Figure 2 below.

The first line is a character string that indicates the presence or absence of the top horizontal line wall as 0 and 1 from the left.
The second line is a character string that indicates the presence or absence of the vertical line wall below it with 0 and 1 from the left.
The third line is a character string that indicates the presence or absence of the wall of the second horizontal line from the top by 0 and 1 from the left.
...
The 9th line is a character string representing the presence or absence of the bottom horizontal line wall with 0 and 1 from the left.


<image>
---
Figure 2 (Thick line shows where the wall is) (corresponding numbers)



However, as shown by the thick line in Fig. 1, it is assumed that there is always a wall for one section to the right of point A. That is, the first character on the first line is always 1.

Output

"Advance one section to the left of the figure" is "L", "Advance one section to the right of the figure" is "R", "Advance one section to the top of the figure" is "U", "Figure" "Advance one block downward" is represented by "D", and "L", "R", "U", and "D" are output in the order of advance.

Example

Input

1111
00001
0110
01011
0010
01111
0010
01001
0111


Output

RRRRDDDDLLLUUURRDDLURULLDDDRRRUUUULLLL
"""

def find_return_path(grid, start_position):
    def print_dir(h):
        if h == 0:
            return 'R'
        elif h == 1:
            return 'D'
        elif h == 2:
            return 'L'
        elif h == 3:
            return 'U'
    
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    hand = 3
    board = [[0 for _ in range(11)] for _ in range(11)]
    
    for i, line in enumerate(grid):
        for j, c in enumerate(line.strip()):
            board[i + 1][1 + (i + 1) % 2 + j * 2] = int(c)
    
    loc = list(start_position)
    path = 'R'
    
    while loc != [1, 1]:
        for i in range(4):
            if board[loc[1] + dir[(hand + i) % 4][1]][loc[0] + dir[(hand + i) % 4][0]] == 1:
                loc[0] += dir[(hand + i) % 4][0] * 2
                loc[1] += dir[(hand + i) % 4][1] * 2
                if i == 1:
                    path += print_dir((hand + 1) % 4)
                elif i == 2:
                    path += print_dir((hand + 2) % 4)
                    hand = (hand + 1) % 4
                elif i == 3:
                    path += print_dir((hand + 3) % 4)
                    hand = (hand + 2) % 4
                elif i == 0:
                    path += print_dir(hand % 4)
                    hand = (hand + 3) % 4
                break
    
    return path