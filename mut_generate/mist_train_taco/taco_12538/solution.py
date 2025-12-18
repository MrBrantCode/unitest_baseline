"""
QUESTION:
Vasya is a Greencode wildlife preservation society proponent. One day he found an empty field nobody owned, divided it into n × m squares and decided to plant a forest there. Vasya will plant nm trees of all different heights from 1 to nm. For his forest to look more natural he wants any two trees growing in the side neighbouring squares to have the absolute value of difference in heights to be strictly more than 1. Help Vasya: make the plan of the forest planting for which this condition is fulfilled.

Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 100) — the number of rows and columns on Vasya's field

Output

If there's no solution, print -1. Otherwise, print n lines containing m numbers each — the trees' planting plan. In every square of the plan the height of a tree that should be planted on this square should be written. If there are several solutions to that problem, print any of them.

Examples

Input

2 3


Output

3 6 2
5 1 4


Input

2 1


Output

-1
"""

def generate_forest_plan(n, m):
    arr = [[0] * m for _ in range(n)]
    
    if m >= 4:
        arr[0] = list(range(m - 1, 0, -2)) + list(range(m, 0, -2))
        for i in range(1, n):
            for j in range(m):
                arr[i][j] = arr[i - 1][j] + m
    elif n >= 4:
        for (ind, i) in enumerate(list(range(n - 1, 0, -2)) + list(range(n, 0, -2))):
            arr[ind][0] = i
        for j in range(1, m):
            for i in range(n):
                arr[i][j] = arr[i][j - 1] + n
    elif n == 2 and m == 3:
        arr = [[3, 6, 2], [5, 1, 4]]
    elif n == 3 and m == 2:
        arr = [[3, 5], [6, 1], [2, 4]]
    elif n == 3 and m == 3:
        arr = [[1, 7, 4], [3, 9, 6], [5, 2, 8]]
    elif n == 1 and m == 1:
        arr = [[1]]
    else:
        return -1
    
    return arr