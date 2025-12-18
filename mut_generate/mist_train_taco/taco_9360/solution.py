"""
QUESTION:
problem

In one programming contest, it is customary to play a bingo game at a social gathering after the competition. However, the bingo card used in this bingo game is a little special and is created according to the following conditions.

* The Bingo card is divided into squares of N rows and N columns, and one positive integer is written in each square. All those integers are different.
* The integer written in the square is 1 or more and M or less.
* The sum of N × N integers written on the Bingo card is S.
* When looking at any column, the integers are arranged in ascending order from top to bottom.
* The integer in every square is larger than any integer in the column to the left of that square.



The following is an example of a Bingo card when N = 5, M = 50, S = 685.

<image>


I want to make as many bingo cards as possible that meet the above conditions for the social gathering. However, you must not make more than one same card. Create a program that outputs the remainder of the maximum number of Bingo cards that can be created divided by 100000.



input

The input consists of multiple datasets. Each dataset is given in the following format.

The input consists of one line, which contains the size of the bingo card N (1 ≤ N ≤ 7), the upper limit of the integers written in the square M (1 ≤ M ≤ 2000), and the bingo card. Three positive integers representing the sum of integers S (1 ≤ S ≤ 3000) are written separated by blanks. However, you can make one or more bingo cards that meet the conditions for any given input data.

When N, M, S is 0, it indicates the end of input. The number of data sets does not exceed 5.

output

For each dataset, divide the maximum number of Bingo cards that can be created by 100000 and output the remainder on one line.

Examples

Input

3 9 45
3 100 50
5 50 685
0 0 0


Output

1
7
74501


Input

None


Output

None
"""

import itertools

def calculate_max_bingo_cards(n, m, s):
    if n == 0:
        return 0
    
    dp = [[0 for _ in range(s + 1)] for _ in range(n * n + 1)]
    dp[0][0] = 1
    
    for (i, j) in itertools.product(range(1, n * n + 1), range(s + 1)):
        if j >= i:
            dp[i][j] += dp[i - 1][j - i] + dp[i][j - i]
        if j - m >= 1:
            dp[i][j] += 100000 - dp[i - 1][j - m - 1]
        dp[i][j] %= 100000
    
    return dp[n * n][s]