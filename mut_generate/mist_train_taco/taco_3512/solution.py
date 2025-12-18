"""
QUESTION:
You have to organize a wedding party. The program of the party will include a concentration game played by the bride and groom. The arrangement of the concentration game should be easy since this game will be played to make the party fun.

We have a 4x4 board and 8 pairs of cards (denoted by `A' to `H') for the concentration game:


+---+---+---+---+
|   |   |   |   |   A A B B
+---+---+---+---+   C C D D
|   |   |   |   |   E E F F
+---+---+---+---+   G G H H
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+


To start the game, it is necessary to arrange all 16 cards face down on the board. For example:


+---+---+---+---+
| A | B | A | B |
+---+---+---+---+
| C | D | C | D |
+---+---+---+---+
| E | F | G | H |
+---+---+---+---+
| G | H | E | F |
+---+---+---+---+


The purpose of the concentration game is to expose as many cards as possible by repeatedly performing the following procedure: (1) expose two cards, (2) keep them open if they match or replace them face down if they do not.

Since the arrangements should be simple, every pair of cards on the board must obey the following condition: the relative position of one card to the other card of the pair must be one of 4 given relative positions. The 4 relative positions are different from one another and they are selected from the following 24 candidates:


(1, 0), (2, 0), (3, 0),
(-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1),
(-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (3, 2),
(-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3).


Your job in this problem is to write a program that reports the total number of board arrangements which satisfy the given constraint. For example, if relative positions (-2, 1), (-1, 1), (1, 1), (1, 2) are given, the total number of board arrangements is two, where the following two arrangements satisfy the given constraint:


X0  X1  X2  X3             X0  X1  X2  X3
+---+---+---+---+          +---+---+---+---+
Y0 | A | B | C | D |       Y0 | A | B | C | D |
+---+---+---+---+          +---+---+---+---+
Y1 | B | A | D | C |       Y1 | B | D | E | C |
+---+---+---+---+          +---+---+---+---+
Y2 | E | F | G | H |       Y2 | F | A | G | H |
+---+---+---+---+          +---+---+---+---+
Y3 | F | E | H | G |       Y3 | G | F | H | E |
+---+---+---+---+          +---+---+---+---+
the relative positions:    the relative positions:
A:(1, 1),  B:(-1, 1)       A:(1, 2),  B:(-1, 1)
C:(1, 1),  D:(-1, 1)       C:(1, 1),  D:(-2, 1)
E:(1, 1),  F:(-1, 1)       E:(1, 2),  F:( 1, 1)
G:(1, 1),  H:(-1, 1)       G:(-2, 1), H:(-1, 1)


Arrangements of the same pattern should be counted only once. Two board arrangements are said to have the same pattern if they are obtained from each other by repeatedly making any two pairs exchange their positions. For example, the following two arrangements have the same pattern:



X0  X1  X2  X3           X0  X1  X2  X3
+---+---+---+---+        +---+---+---+---+
Y0 | H | G | F | E |     Y0 | A | B | C | D |
+---+---+---+---+        +---+---+---+---+
Y1 | G | E | D | F |     Y1 | B | D | E | C |
+---+---+---+---+        +---+---+---+---+
Y2 | C | H | B | A |     Y2 | F | A | G | H |
+---+---+---+---+        +---+---+---+---+
Y3 | B | C | A | D |     Y3 | G | F | H | E |
+---+---+---+---+        +---+---+---+---+


where (1) `A' and `H', (2) `B' and `G', (3) `C' and `F', and (4) `D' and `E' exchange their positions respectively.



Input

The input contains multiple data sets, each representing 4 relative positions. A data set is given as a line in the following format.

x1| y1 | x2| y2 | x3| y3 | x4| y4
---|---|---|---|---|---|---|---

The i-th relative position is given by (xi, yi). You may assume that the given relative positions are different from one another and each of them is one of the 24 candidates.

The end of input is indicated by the line which contains a single number greater than 4.

Output

For each data set, your program should output the total number of board arrangements (or more precisely, the total number of patterns).

Each number should be printed in one line. Since your result is checked by an automatic grading program, you should not insert any extra characters nor lines on the output.

Examples

Input




Output




Input

-2 1 -1 1 1 1 1 2
1 0 2 1 2 2 3 3
5


Output

2
15
"""

def count_valid_arrangements(relative_positions):
    def combi(k):
        nonlocal ans
        if k == 9:
            ans += 1
            return
        for y in range(4):
            for x in range(4):
                if arr[y][x]:
                    continue
                arr[y][x] = k
                for i in range(4):
                    x2, y2 = x + relative_positions[i][0], y + relative_positions[i][1]
                    if x2 < 0 or x2 >= 4 or y2 < 0 or y2 >= 4 or arr[y2][x2]:
                        continue
                    arr[y2][x2] = k
                    combi(k + 1)
                    arr[y2][x2] = 0
                arr[y][x] = 0
                return

    arr = [[0 for _ in range(4)] for _ in range(4)]
    ans = 0
    arr[0][0] = 1
    for i in range(4):
        x, y = relative_positions[i]
        if x >= 0 and y >= 0:
            arr[y][x] = 1
            combi(2)
            arr[y][x] = 0
    return ans