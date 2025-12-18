"""
QUESTION:
Given an N x N grid, a list of lamps, and a list of queries, determine the illumination status of each query cell. A cell is illuminated if it is in the same row, column, or diagonal as a lamp. The function should return a list of integers where 1 represents an illuminated cell and 0 represents an unilluminated cell. The function should also turn off lamps that are in the surrounding cells of an illuminated query cell (horizontally, vertically, or diagonally adjacent).

The function should be named gridIllumination and take three parameters: N (the size of the grid), lamps (a list of lamp coordinates), and queries (a list of query cell coordinates).
"""

def gridIllumination(N, lamps, queries):
    from collections import defaultdict
    lamp_pos = set()
    rows, cols, diags, anti_diags = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)

    # Turn on lamps and update hashmaps
    for x, y in lamps:
        lamp_pos.add((x,y))
        rows[x] += 1
        cols[y] += 1
        diags[x-y] += 1
        anti_diags[x+y] += 1

    ans = []
    for x, y in queries:
        # check if cell is illuminated
        if rows[x] > 0 or cols[y] > 0 or diags[x-y] > 0 or anti_diags[x+y] > 0:
            ans.append(1)
        else:
            ans.append(0)

        # turn off surrounding lamps, if they exist
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x+dx, y+dy
                if (nx, ny) in lamp_pos:
                    lamp_pos.remove((nx, ny))
                    rows[nx] -= 1
                    cols[ny] -= 1
                    diags[nx-ny] -= 1
                    anti_diags[nx+ny] -= 1

    return ans