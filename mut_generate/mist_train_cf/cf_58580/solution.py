"""
QUESTION:
gridIllumination function takes four parameters: an integer N representing the dimensions of a grid, a list of lamp positions lamps, and a list of query positions queries. The function must return an array of integers where each integer corresponds to whether the lamp at the query position is illuminated or not. 

The function must follow these rules: 
- Initially, all lamps are off. 
- When a lamp is activated, it illuminates its own cell and all other cells in the same row, column, or diagonal. 
- After responding to a query, deactivate the lamp at the query position and its 8 neighboring lamps, if they exist. 
- The constraints are: 1 <= N <= 10^9, 0 <= lamps.length <= 20000, and 0 <= queries.length <= 20000.
"""

def gridIllumination(N, lamps, queries):
    from collections import defaultdict
    lamp_pos = set()
    rows, cols, diags, anti_diags = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    
    # turn on lamps and update hashmaps
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