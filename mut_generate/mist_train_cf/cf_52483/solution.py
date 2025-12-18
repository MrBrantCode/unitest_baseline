"""
QUESTION:
Find the total area covered by all rectangles in the plane. You are given a list of rectangles where each rectangle[i] = [xi1, yi1, xi2, yi2], with (xi1, yi1) as the coordinates of the bottom-left corner and (xi2, yi2) as the coordinates of the top-right corner of the ith rectangle. Some rectangles may overlap with each other. When overlapping, consider the overlapping sections only once in the total area calculation. Return the total area modulo 10^9 + 7.

The given list of rectangles is denoted as rectangles, where 1 <= rectangles.length <= 500 and rectangles[i].length = 4. Each coordinate is within the range 0 <= rectangles[i][j] <= 10^9. The total area covered by all rectangles will never exceed 2^63 - 1.
"""

def rectangleArea(rectangles):
    OPEN, CLOSE = range(2)
    events = []
    Y = set()
    for rec in rectangles:
        x1, y1, x2, y2 = rec
        events.append((x1, OPEN , y1, y2))
        events.append((x2, CLOSE, y1, y2))
        Y.add(y1)
        Y.add(y2)

    events.sort()
    Y = sorted(list(Y))

    iY = {y : i for i, y in enumerate(Y)}

    ST = {}
    def update(i, j, val):
        if i >= j: return
        ST[(i, j)] = [ST.get((i, j), [0,0])[0] + val, 0]
        if val and j-i == 1:
            ST[(i, j)][1] = Y[j] - Y[i]
        else: 
            mid = (i + j) // 2
            update(i, mid, val)
            update(mid, j, val)
            ST[(i, j)][1] = ST.get((i, mid), [0,0])[1]*(ST.get((i, mid), [0,0])[0] > 0) + ST.get((mid, j), [0,0])[1]*(ST.get((mid, j), [0,0])[0] > 0)
        return

    def query(i, j, X, val = 1):
        if ST.get((i, j), [0,0])[0]:
            return ST[(i, j)][1]
        elif j - i <= 1:
            return 0
        elif X < Y[(i + j) // 2]:
            return query(i, (i + j) // 2, X)
        else:
            return ST.get((i, (i + j) // 2), [0,0])[1] + query((i + j) // 2, j, X)

    res = 0
    cur_x_sum = query(0, len(Y), events[0][0])

    for i in range(1, len(events)):
        x, kind, y1, y2 = events[i]
        res += (x - events[i-1][0])*cur_x_sum
        update(iY[y1], iY[y2], 1 if kind is OPEN else -1)
        cur_x_sum = query(0, len(Y), x)

    return res % (10**9+7)