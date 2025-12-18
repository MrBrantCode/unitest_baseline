"""
QUESTION:
Mr. Bender has a digital table of size n × n, each cell can be switched on or off. He wants the field to have at least c switched on squares. When this condition is fulfilled, Mr Bender will be happy.

We'll consider the table rows numbered from top to bottom from 1 to n, and the columns — numbered from left to right from 1 to n. Initially there is exactly one switched on cell with coordinates (x, y) (x is the row number, y is the column number), and all other cells are switched off. Then each second we switch on the cells that are off but have the side-adjacent cells that are on.

For a cell with coordinates (x, y) the side-adjacent cells are cells with coordinates (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1).

In how many seconds will Mr. Bender get happy?

Input

The first line contains four space-separated integers n, x, y, c (1 ≤ n, c ≤ 109; 1 ≤ x, y ≤ n; c ≤ n2).

Output

In a single line print a single integer — the answer to the problem.

Examples

Input

6 4 3 1


Output

0


Input

9 3 8 10


Output

2

Note

Initially the first test has one painted cell, so the answer is 0. In the second test all events will go as is shown on the figure. <image>.
"""

def suma_impares(m):
    return m * m

def suma_n(m):
    return m * (m - 1) // 2

def cnt(t, x, y, n):
    (u, d, l, r) = (x + t, x - t, y - t, y + t)
    suma = t ** 2 + (t + 1) ** 2
    if u > n:
        suma -= suma_impares(u - n)
    if d < 1:
        suma -= suma_impares(1 - d)
    if l < 1:
        suma -= suma_impares(1 - l)
    if r > n:
        suma -= suma_impares(r - n)
    if 1 - l > x - 1 and 1 - d > y - 1:
        suma += suma_n(2 - l - x)
    if r - n > x - 1 and 1 - d > n - y:
        suma += suma_n(r - n - x + 1)
    if 1 - l > n - x and u - n > y - 1:
        suma += suma_n(1 - l - n + x)
    if u - n > n - y and r - n > n - x:
        suma += suma_n(u - n - n + y)
    return suma

def calculate_happiness_time(n, x, y, c):
    (ini, fin) = (0, int(1000000000.0))
    cont = int(1000000000.0)
    while cont > 0:
        m = ini
        paso = cont // 2
        m += paso
        if cnt(m, x, y, n) < c:
            ini = m + 1
            cont -= paso + 1
        else:
            cont = paso
    return ini