"""
QUESTION:
Polycarp has a checkered sheet of paper of size n × m. Polycarp painted some of cells with black, the others remained white. Inspired by Malevich's "Black Square", Polycarp wants to paint minimum possible number of white cells with black so that all black cells form a square.

You are to determine the minimum possible number of cells needed to be painted black so that the black cells form a black square with sides parallel to the painting's sides. All the cells that do not belong to the square should be white. The square's side should have positive length.


-----Input-----

The first line contains two integers n and m (1 ≤ n, m ≤ 100) — the sizes of the sheet.

The next n lines contain m letters 'B' or 'W' each — the description of initial cells' colors. If a letter is 'B', then the corresponding cell is painted black, otherwise it is painted white.


-----Output-----

Print the minimum number of cells needed to be painted black so that the black cells form a black square with sides parallel to the painting's sides. All the cells that do not belong to the square should be white. If it is impossible, print -1.


-----Examples-----
Input
5 4
WWWW
WWWB
WWWB
WWBB
WWWW

Output
5

Input
1 2
BB

Output
-1

Input
3 3
WWW
WWW
WWW

Output
1



-----Note-----

In the first example it is needed to paint 5 cells — (2, 2), (2, 3), (3, 2), (3, 3) and (4, 2). Then there will be a square with side equal to three, and the upper left corner in (2, 2).

In the second example all the cells are painted black and form a rectangle, so it's impossible to get a square.

In the third example all cells are colored white, so it's sufficient to color any cell black.
"""

def min_cells_to_form_square(n, m, canvas):
    def find_top():
        for i in range(n):
            for j in range(m):
                if canvas[i][j] == 'B':
                    return i
        return -1

    def find_left():
        for j in range(m):
            for i in range(n):
                if canvas[i][j] == 'B':
                    return j

    def find_bottom():
        for i in reversed(range(n)):
            for j in range(m):
                if canvas[i][j] == 'B':
                    return i

    def find_right():
        for j in reversed(range(m)):
            for i in range(n):
                if canvas[i][j] == 'B':
                    return j

    t = find_top()
    if t == -1:
        return 1
    l = find_left()
    b = find_bottom()
    r = find_right()

    painted = 0
    for i in range(t, b + 1):
        for j in range(l, r + 1):
            if canvas[i][j] == 'W':
                painted += 1

    while b - t < r - l:
        if t > 0:
            t -= 1
            painted += r - l + 1
        elif b < n - 1:
            b += 1
            painted += r - l + 1
        else:
            return -1

    while r - l < b - t:
        if l > 0:
            l -= 1
            painted += b - t + 1
        elif r < m - 1:
            r += 1
            painted += b - t + 1
        else:
            return -1

    return painted