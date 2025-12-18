"""
QUESTION:
One day Alex decided to remember childhood when computers were not too powerful and lots of people played only default games. Alex enjoyed playing Minesweeper that time. He imagined that he saved world from bombs planted by terrorists, but he rarely won.

Alex has grown up since then, so he easily wins the most difficult levels. This quickly bored him, and he thought: what if the computer gave him invalid fields in the childhood and Alex could not win because of it?

He needs your help to check it.

A Minesweeper field is a rectangle $n \times m$, where each cell is either empty, or contains a digit from $1$ to $8$, or a bomb. The field is valid if for each cell:   if there is a digit $k$ in the cell, then exactly $k$ neighboring cells have bombs.  if the cell is empty, then all neighboring cells have no bombs. 

Two cells are neighbors if they have a common side or a corner (i. e. a cell has at most $8$ neighboring cells).


-----Input-----

The first line contains two integers $n$ and $m$ ($1 \le n, m \le 100$) — the sizes of the field.

The next $n$ lines contain the description of the field. Each line contains $m$ characters, each of them is "." (if this cell is empty), "*" (if there is bomb in this cell), or a digit from $1$ to $8$, inclusive.


-----Output-----

Print "YES", if the field is valid and "NO" otherwise.

You can choose the case (lower or upper) for each letter arbitrarily.


-----Examples-----
Input
3 3
111
1*1
111

Output
YES
Input
2 4
*.*.
1211

Output
NO


-----Note-----

In the second example the answer is "NO" because, if the positions of the bombs are preserved, the first line of the field should be *2*1.

You can read more about Minesweeper in Wikipedia's article.
"""

def is_valid_minesweeper_field(n, m, field):
    def pos(x, num):
        if x < 0:
            return -1
        elif x >= num:
            return -1
        return x

    def check(x, y, ai, n, m):
        num = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if pos(x + i, n) == -1 or pos(y + j, m) == -1:
                    continue
                if ai[pos(x + i, n)][pos(y + j, m)] == '*':
                    num += 1
        return num

    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                continue
            temp = 0
            if field[i][j] != '.':
                temp = int(field[i][j])
            if temp != check(i, j, field, n, m):
                return False
    return True