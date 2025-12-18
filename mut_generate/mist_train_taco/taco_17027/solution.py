"""
QUESTION:
Bishwock is a chess figure that consists of three squares resembling an "L-bar". This figure can be rotated by 90, 180 and 270 degrees so it can have four possible states:

 

XX   XX   .X   X.

X.   .X   XX   XX

 

Bishwocks don't attack any squares and can even occupy on the adjacent squares as long as they don't occupy the same square. 

Vasya has a board with $2\times n$ squares onto which he wants to put some bishwocks. To his dismay, several squares on this board are already occupied by pawns and Vasya can't put bishwocks there. However, pawns also don't attack bishwocks and they can occupy adjacent squares peacefully.

Knowing the positions of pawns on the board, help Vasya to determine the maximum amount of bishwocks he can put onto the board so that they wouldn't occupy the same squares and wouldn't occupy squares with pawns.


-----Input-----

The input contains two nonempty strings that describe Vasya's board. Those strings contain only symbols "0" (zero) that denote the empty squares and symbols "X" (uppercase English letter) that denote the squares occupied by pawns. Strings are nonempty and are of the same length that does not exceed $100$.


-----Output-----

Output a single integer — the maximum amount of bishwocks that can be placed onto the given board.


-----Examples-----
Input
00
00

Output
1
Input
00X00X0XXX0
0XXX0X00X00

Output
4
Input
0X0X0
0X0X0

Output
0
Input
0XXX0
00000

Output
2
"""

def max_bishwocks(row1: str, row2: str) -> int:
    ct = 0
    i = 0
    while i < len(row1):
        if i + 1 < len(row1) and row1[i] == '0' and row1[i + 1] == '0' and row2[i] == '0' and row2[i + 1] == '0':
            ct += 1
            i += 2
        elif i + 2 < len(row1) and row1[i] == '0' and row1[i + 1] == '0' and row1[i + 2] == '0' and row2[i] == '0' and row2[i + 1] == '0' and row2[i + 2] == '0':
            ct += 2
            i += 3
        else:
            i += 1
    return ct