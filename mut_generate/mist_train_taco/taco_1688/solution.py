"""
QUESTION:
The Chef has a huge square napkin of size 2n X 2n. He folds the napkin n-3 times. Each time he folds its bottom side over its top side, and then its right side over its left side. After each fold, the side length of the napkin is reduced by half. The Chef continues folding until there remains a 8x8 sheet, lying flat on a table.
Oh, did I forget to mention that the Chef was cooking a new brown colored curry while folding the napkin. He drops some brown colored gravy onto some cells in the folded 8x8 napkin. When he drops the gravy, it soaks through all the cells below it.
Now the Chef unfolds the napkin to its original size. There are now many curry stained brown colored cells in the napkin. They form several separate regions, each of which is connected. Could you help the Chef count how many regions of brown cells are there in the napkin?
Note that two cells are adjacent if they share a common edge (they are not considered adjacent if they only share a corner). Two cells are connected if we can go from one cell to the other via adjacent cells. A region is a maximal set of cells such that every two of its cells are connected.
Please see the example test case for more details.

-----Input-----
The first line contains t, the number of test cases (about 50). Then t test cases follow. Each test case has the following form:
- The first line contains N (3 ≤ N ≤ 109)
- Then, 8 lines follow. Each line is a string of 8 characters, 0 or 1, where 1 denotes a stained brown cell in the folded napkin.

-----Output-----
For each test case, print a single number that is the number of disconnected brown regions in the unfolded napkin. Since the result may be a very large number, you only need to print its remainder when dividing by 21945.

-----Example-----
Input:
3
3
01000010
11000001
00000000
00011000
00011000
00010100
00001000
00000000
4
01000010
11000001
00000000
00011000
00011000
00010100
00001000
00000000
1000000000
11111111
11111111
11111111
11111111
11111111
11111111
11111111
11111111

Output:
6
22
1

-----Output details-----

Case 1 and 2: There are 6 brown regions in the 8x8 napkin. If we unfold it once, it has 22 brown regions: 11 regions in the top half and 11 regions in the bottom half (as shown in the figure above).
Case 3: All cells of the napkin are stained, so there is always one brown region, no matter how many times the Chef unfolds the napkin.
"""

def count_brown_regions(n, brown_cells):
    def identify(x, y):
        rows[x][y] = '2'
        r = 0
        if x == 0:
            r |= 1
        elif rows[x - 1][y] == '1':
            r |= identify(x - 1, y)
        if x == 7:
            r |= 4
        elif rows[x + 1][y] == '1':
            r |= identify(x + 1, y)
        if y == 0:
            r |= 2
        elif rows[x][y - 1] == '1':
            r |= identify(x, y - 1)
        if y == 7:
            r |= 8
        elif rows[x][y + 1] == '1':
            r |= identify(x, y + 1)
        return r

    P = 21945
    n -= 3
    rows = [list(row) for row in brown_cells]
    total = 0

    for i in range(8):
        for j in range(8):
            if rows[i][j] == '1':
                r = identify(i, j)
                if n == 0:
                    total += 1
                    continue
                if r == 0:
                    total += pow(2, 2 * n, P)
                elif r == 1 or r == 2 or r == 4 or r == 8:
                    total += pow(2, 2 * n - 1, P)
                    if r == 1 or r == 2:
                        total += pow(2, n, P)
                elif r == 5 or r == 10:
                    total += pow(2, n, P)
                elif r == 3 or r == 6 or r == 12 or r == 9:
                    total += pow(2, 2 * n - 2, P)
                    if r == 3:
                        total += 3 + 2 * pow(2, n - 1, P) - 2
                    elif r == 6 or r == 9:
                        total += pow(2, n - 1, P)
                elif r == 15:
                    total += 1
                else:
                    total += pow(2, n - 1, P)
                    if r == 11 or r == 7:
                        total += 1

    return total % P