"""
QUESTION:
Write a function `largest_product_of_three_regions(grid)` that takes a 2D grid as input, where 0 represents an empty cell and 9 represents an obstacle. The function should return the largest product of the sizes of three connected regions of empty cells. Two cells are considered connected if they are adjacent horizontally or vertically and both are empty. If there are fewer than three connected regions of empty cells, return 0.
"""

def largest_product_of_three_regions(grid):
    rlen, clen = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    checked = set()
    ans = []

    def dfs(r, c):
        size = 0
        s = [(r, c)]
        while s:
            nr, nc = s.pop()
            size += 1
            for ar, ac in directions:
                ar = nr + ar
                ac = nc + ac
                if (ar, ac) not in checked and (0 <= ar < rlen) and (0 <= ac < clen) and (grid[ar][ac] == 0):
                    s.append((ar, ac))
                    checked.add((ar, ac))
        return size

    for r in range(rlen):
        for c in range(clen):
            if grid[r][c] == 0 and (r, c) not in checked:
                ans.append(dfs(r, c))
                checked.add((r, c))

    ans.sort()
    return ans[-1] * ans[-2] * ans[-3] if len(ans) >= 3 else 0