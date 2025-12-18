"""
QUESTION:
Queens on Board

You have an N * M chessboard on which some squares are blocked out. In how many ways can you place one or more queens on the board, such that, no two queens attack each other? Two queens attack each other, if one can reach the other by moving horizontally, vertically, or diagonally without passing over any blocked square. At most one queen can be placed on a square. A queen cannot be placed on a blocked square.

Input Format

The first line contains the number of test cases T. T test cases follow. Each test case contains integers N and M on the first line. The following N lines contain M characters each, and represent a board. A '#' represents a blocked square and a '.' represents an unblocked square.

Constraints

1 <= T <= 100 

1 <= N <= 50 

1 <= M <= 5

Output Format

Output T lines containing the required answer for each test case. As the answers can be really large, output them modulo 10^{9}+7.

Sample Input
4  
3 3  
...  
...  
...  
3 3  
.#.  
.#.  
...  
2 4  
.#..  
....  
1 1  
#

Sample Output
17  
18  
14  
0
"""

def count_queen_placements(test_cases):
    mod = 1000000007
    
    def memoize(func):
        pool = {}
        def wrapper(*arg):
            if arg not in pool:
                pool[arg] = func(*arg)
            return pool[arg]
        return wrapper
    
    def is_wall(x, y, mx, X, Y):
        return mx[y] & 1 << x != 0 if 0 <= x < X and 0 <= y < Y else True
    
    def get_free(mx, X, Y):
        y = 0
        while y < Y and mx[y] == (1 << X) - 1:
            y += 1
        if y == Y:
            return (None, None)
        free = 0
        while mx[y] & 1 << free != 0:
            free += 1
        if free >= X:
            return (None, None)
        return (free, y)
    
    def place_queen(x, y, mx, X, Y):
        nmx = list(mx)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                (cx, cy) = (x, y)
                while not is_wall(cx, cy, nmx, X, Y):
                    nmx[cy] |= 1 << cx
                    (cx, cy) = (cx + dx, cy + dy)
        return tuple(nmx)
    
    @memoize
    def rec(mx, X, Y):
        (free_x, free_y) = get_free(mx, X, Y)
        if free_x is None:
            return 0
        imx = list(mx)
        imx[free_y] |= 1 << free_x
        ans = rec(tuple(imx), X, Y)
        nmx = place_queen(free_x, free_y, mx, X, Y)
        ans += 1
        (free_x, free_y) = get_free(nmx, X, Y)
        if free_x is not None:
            ans += rec(nmx, X, Y)
        return ans % mod
    
    results = []
    for (N, M, board) in test_cases:
        mx = [int(''.join(('0' if c == '.' else '1' for c in row)), 2) for row in board]
        results.append(rec(tuple(mx), M, N))
    
    return results