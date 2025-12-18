"""
QUESTION:
jfen

There is a one-person game to play on the H × W board. This game is a game to move 0 or 1 balls in each cell. You were playing this game and found it difficult to move the ball accurately from cell to cell because the ball is so round. So you decided to make a robot that would move the ball as instructed. Here, the notation (y, x) is used to represent the cell. This represents the cell in the xth column of the yth row.

Instructions to the robot are given by the four integers a, b, c, d. This means moving the ball at (a, b) to (c, d). At this time, it is guaranteed that the ball exists in (a, b) and does not exist in (c, d).

The state of the board is expressed by the following notation called "jfen".


[Data in the first line] / [Data in the second line] /.../ [Data in the H line]

This notation is a slash-separated concatenation of data representing each line on the board. The data in each row is represented by a character string, and the state of the cells in the 1st to Wth columns is described in order from the left. This string is represented by a number and the letter'b', where the integer represented by the number represents the number of consecutive blank cells and'b' represents the cell in which the ball resides. Here, integers must not be consecutive in the data of each row. Also, the sum of the integers written in the data of each line and the sum of the number of'b'are always W.

As an example, consider the following board surface condition. A blank cell is represented by a'.', And a cell in which the ball exists is represented by a'b'. The j character from the left of the i-th row in this example represents the state of the cell in the j-th column of the i-th row on the board.


....
.b.b
....


The above board is expressed in jfen as follows.


4 / 1b1b / 4

Create a program that outputs the board surface after the robot moves the ball when the robot is given the current board surface state and a command to move one ball. At this time, output the board surface in jfen notation.

Input

The input consists of multiple datasets. Each dataset has the following format.

> S
> a b c d

Each dataset consists of two lines, and the first line is given the jfen-formatted string S, which represents the state of the board. Here, the size of the board satisfies 2 ≤ W and H ≤ 9. Instructions to the robot are given to the following lines. This represents an instruction to move the ball at (a, b) to (c, d). The end of the input is represented by #.

Output

The output is one line of character string that expresses the state of the board after executing the instruction for each data set in jfen notation. There must be no other characters on the output line.

Sample Input


b1 / 1b
1 1 1 2
b5 / bbbbbb
2 4 1 4
b2b2b / 7
1 4 2 4


Output for Sample Input


1b / 1b
b2b2 / bbb1bb
b5b / 3b3


The initial state of the first input is as follows.


b.
.b


Since the ball of (1,1) is moved to (1,2), the board surface after the command is as follows.


.b
.b






Example

Input

b1/1b
1 1 1 2
b5/bbbbbb
2 4 1 4
b2b2b/7
1 4 2 4
#


Output

1b/1b
b2b2/bbb1bb
b5b/3b3
"""

def move_ball_on_board(jfen_string, a, b, c, d):
    # Split the jfen string into rows
    rows = jfen_string.split('/')
    H = len(rows)
    W = sum(len(row) for row in rows) // H
    
    # Convert jfen string to a 2D list representing the board
    board = []
    for row in rows:
        board_row = []
        i = 0
        while i < len(row):
            if row[i] == 'b':
                board_row.append(1)
                i += 1
            else:
                num = ''
                while i < len(row) and row[i].isdigit():
                    num += row[i]
                    i += 1
                board_row.extend([0] * int(num))
        board.append(board_row)
    
    # Move the ball
    board[a - 1][b - 1] = 0
    board[c - 1][d - 1] = 1
    
    # Convert the board back to jfen notation
    result = []
    for row in board:
        jfen_row = ''
        i = 0
        while i < len(row):
            if row[i] == 1:
                jfen_row += 'b'
                i += 1
            else:
                count = 0
                while i < len(row) and row[i] == 0:
                    count += 1
                    i += 1
                jfen_row += str(count)
        result.append(jfen_row)
    
    return '/'.join(result)