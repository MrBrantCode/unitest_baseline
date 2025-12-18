"""
QUESTION:
Sugoroku

problem

JOI is playing sugoroku alone. There are N squares in a straight line in this sugoroku, and each has a movement instruction written on it. The starting point is the 1st square and the goal is the Nth square. JOI repeats the following until he reaches the goal.

Roll the dice and proceed from the current square by the number of rolls, and follow the instructions of that square. Do not follow the instructions of the square to which you moved according to the instructions.

The goal is not only when you stop at the Nth square, but also when the destination exceeds the Nth square.

Create a program that outputs how many times you roll the dice to reach the goal when you are given a sugoroku board and M dice rolls.

input

The input consists of multiple datasets. Each dataset is given in the following format.

Each dataset consists of 1 + N + M rows.

Two integers N, M (2 ≤ N ≤ 1000, 1 ≤ M ≤ 1000) are written on the first line of the input, separated by blanks. N represents the number of sugoroku squares, and M represents the number of dice given.

In the following N lines, integers between -999 and 999 are written one by one. The integer on the 1 + i line (1 ≤ i ≤ N) represents the indication of the sugoroku i-th cell. Let X be the written integer. When X = 0, it indicates "do nothing", when X> 0, it indicates "advance X mass", and when X <0, it indicates "| X | mass return". However, | X | represents the absolute value of X.

In the following M line, integers from 1 to 6 are written one by one, and the number on the 1 + N + j line (1 ≤ j ≤ M) represents the dice roll that appears on the jth time.

However, the number of lines 2 and 1 + N is always 0. There is no cell with instructions to move to the cell before the first cell. In addition, the number of times the dice are rolled is M or less in any scoring input data.

When both N and M are 0, it indicates the end of input. The number of data sets does not exceed 5.

output

For each data set, an integer indicating how many times the dice are rolled to reach the goal is output on one line.

Input / output example

Input example


10 5
0
0
Five
6
-3
8
1
8
-Four
0
1
3
Five
1
Five
10 10
0
-1
-1
Four
Four
-Five
0
1
-6
0
1
Five
2
Four
6
Five
Five
Four
1
6
0 0


Output example


Five
6


The following figure shows the first input example.
<image>

The following figure shows the second input example.
<image>

The above question sentences and the data used for the automatic referee are the question sentences created and published by the Japan Committee for Information Olympics and the test data for scoring.





Example

Input

10 5
0
0
5
6
-3
8
1
8
-4
0
1
3
5
1
5
10 10
0
-1
-1
4
4
-5
0
1
-6
0
1
5
2
4
6
5
5
4
1
6
0 0


Output

5
6
"""

def sugoroku_game(N, M, S, dice_rolls):
    p = 1  # Starting position
    for i in range(M):
        d = dice_rolls[i]
        p += d
        if p >= N:
            return i + 1
        p += S[p - 1]
        if p >= N:
            return i + 1
    return M  # In case the loop completes without reaching the goal