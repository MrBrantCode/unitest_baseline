"""
QUESTION:
Chain Disappearance Puzzle

We are playing a puzzle. An upright board with H rows by 5 columns of cells, as shown in the figure below, is used in this puzzle. A stone engraved with a digit, one of 1 through 9, is placed in each of the cells. When three or more stones in horizontally adjacent cells are engraved with the same digit, the stones will disappear. If there are stones in the cells above the cell with a disappeared stone, the stones in the above cells will drop down, filling the vacancy.


<image>


The puzzle proceeds taking the following steps.

1. When three or more stones in horizontally adjacent cells are engraved with the same digit, the stones will disappear. Disappearances of all such groups of stones take place simultaneously.
2. When stones are in the cells above the emptied cells, these stones drop down so that the emptied cells are filled.
3. After the completion of all stone drops, if one or more groups of stones satisfy the disappearance condition, repeat by returning to the step 1.



The score of this puzzle is the sum of the digits on the disappeared stones.

Write a program that calculates the score of given configurations of stones.


<image>


Input

The input consists of multiple datasets. Each dataset is formed as follows.

> Board height H
>  Stone placement of the row 1
>  Stone placement of the row 2
>  ...
>  Stone placement of the row H
>

The first line specifies the height ( H  ) of the puzzle board (1 ≤ H ≤ 10). The remaining H lines give placement of stones on each of the rows from top to bottom. The placements are given by five digits (1 through 9), separated by a space. These digits are engraved on the five stones in the corresponding row, in the same order.

The input ends with a line with a single zero.

Output

For each dataset, output the score in a line. Output lines may not include any characters except the digits expressing the scores.

Sample Input


1
6 9 9 9 9
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
10
3 5 6 5 6
2 2 2 8 3
6 2 5 9 2
7 7 7 6 1
4 6 6 4 9
8 9 1 1 8
5 6 1 8 1
6 8 2 1 2
9 6 3 3 5
5 3 8 8 8
5
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
3
2 2 8 7 4
6 5 7 7 7
8 8 9 9 9
0


Output for the Sample Input


36
38
99
0
72






Example

Input

1
6 9 9 9 9
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
10
3 5 6 5 6
2 2 2 8 3
6 2 5 9 2
7 7 7 6 1
4 6 6 4 9
8 9 1 1 8
5 6 1 8 1
6 8 2 1 2
9 6 3 3 5
5 3 8 8 8
5
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
3
2 2 8 7 4
6 5 7 7 7
8 8 9 9 9
0


Output

36
38
99
0
72
"""

def calculate_puzzle_score(board_height, stone_placements):
    from functools import lru_cache

    def DEBUG(*args):
        pass

    @lru_cache(maxsize=None)
    def pat(s, n):
        return ' '.join([s] * n)

    def removeAll(xs, s):
        while s in xs:
            xs.remove(s)
            xs.append('#')
        return xs

    def lmap(f, s):
        return list(map(f, s))

    digits = lmap(str, range(1, 10))

    data = '\n'.join([' '.join(map(str, row)) for row in stone_placements])
    score = 0
    DEBUG(data)

    while True:
        removed = False
        sum1 = sum(map(lambda x: 0 if x == '#' else int(x), data.split()))
        for d in digits:
            if pat(d, 3) in data:
                data = data.replace(pat(d, 5), pat('0', 5))
                data = data.replace(pat(d, 4), pat('0', 4))
                data = data.replace(pat(d, 3), pat('0', 3))
                removed = True
        if not removed:
            break
        DEBUG(data)
        score += sum1 - sum(map(lambda x: 0 if x == '#' else int(x), data.split()))
        data = zip(*map(lambda x: x.split(), data.split('\n')))
        data = map(lambda x: list(x[::-1]), data)
        data = map(lambda x: removeAll(x, '0'), data)
        data = lmap(lambda s: ' '.join(s), zip(*data))
        data = '\n'.join(data[::-1])
        DEBUG(data)

    return score