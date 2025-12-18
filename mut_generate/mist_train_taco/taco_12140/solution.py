"""
QUESTION:
Rabbits and cats are competing. The rules are as follows.

First, each of the two animals wrote n2 integers on a piece of paper in a square with n rows and n columns, and drew one card at a time. Shuffle two cards and draw them one by one alternately. Each time a card is drawn, the two will mark it if the same number as the card is written on their paper. The winning condition is that the number of "a set of n numbers with a mark and is in a straight line" is equal to or greater than the number of playing cards drawn at the beginning.

Answer which of the rabbit and the cat wins up to the mth card given. However, the victory or defeat is when only one of the two cards meets the victory condition when a certain card is drawn and marked. In other cases, it is a draw. Cards may be drawn even after one of them meets the victory conditions, but this does not affect the victory or defeat.



Input

Line 1: “nuvm” (square size, number of rabbit playing cards, number of cat playing cards, number of cards drawn) 2- (N + 1) Line: n2 numbers that the rabbit writes on paper ( N + 2)-(2N + 1) Line: n2 numbers that the cat writes on paper (2N + 2)-(2N + M + 1) Line: m cards drawn
1 ≤ n ≤ 500
1 ≤ u, v ≤ 13
1 ≤ m ≤ 100 000
1 ≤ (number written) ≤ 1 000 000


The number of n2 rabbits write on paper, the number of n2 cats write on paper, and the number of m cards drawn are different.

Output

Output "USAGI" if the rabbit wins, "NEKO" if the cat wins, and "DRAW" if the tie, each in one line.

Examples

Input

3 2 2 10
1 2 3
4 5 6
7 8 9
1 2 3
6 5 4
7 8 9
11
4
7
5
10
9
2
1
3
8


Output

USAGI


Input

3 2 1 10
1 2 3
4 5 6
7 8 9
1 2 3
6 5 4
7 8 9
11
4
7
5
10
9
2
1
3
8


Output

DRAW
"""

def determine_winner(n, u, v, m, rabbit_grid, cat_grid, drawn_cards):
    usadic = {}
    nekodic = {}
    usatable = [0 for i in range(2 * n + 2)]
    nekotable = [0 for i in range(2 * n + 2)]
    
    # Populate the dictionaries with positions of numbers in the grids
    for i in range(n):
        for j in range(n):
            usadic[rabbit_grid[i][j]] = []
            nekodic[cat_grid[i][j]] = []
            usadic[rabbit_grid[i][j]].append(i)
            nekodic[cat_grid[i][j]].append(i)
            usadic[rabbit_grid[i][j]].append(n + j)
            nekodic[cat_grid[i][j]].append(n + j)
            if i == j:
                usadic[rabbit_grid[i][j]].append(2 * n)
                nekodic[cat_grid[i][j]].append(2 * n)
            if i + j == n - 1:
                usadic[rabbit_grid[i][j]].append(2 * n + 1)
                nekodic[cat_grid[i][j]].append(2 * n + 1)
    
    usacount = 0
    nekocount = 0
    
    # Process each drawn card
    for t in drawn_cards:
        if t in usadic:
            for x in usadic[t]:
                usatable[x] += 1
                if usatable[x] == n:
                    usacount += 1
        if t in nekodic:
            for x in nekodic[t]:
                nekotable[x] += 1
                if nekotable[x] == n:
                    nekocount += 1
        if n == 1:
            usacount = min(usacount, 1)
            nekocount = min(nekocount, 1)
        if usacount >= u and nekocount >= v:
            return 'DRAW'
        elif usacount >= u:
            return 'USAGI'
        elif nekocount >= v:
            return 'NEKO'
    
    return 'DRAW'