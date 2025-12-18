"""
QUESTION:
Example

Input

2 4
%.@\$
..\$\$


Output

Yes
"""

import queue

def can_reach_goal(h, w, field):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    pdist = [[1000] * w for _ in range(h)]
    sdist = [[1000] * w for _ in range(h)]
    pque = queue.Queue()
    sque = queue.Queue()
    
    for i, row in enumerate(field):
        for j in range(w):
            if row[j] == '@':
                pque.put((i, j))
                pdist[i][j] = 0
            if row[j] == '$':
                sque.put((i, j))
                sdist[i][j] = 0
            if row[j] == '%':
                gi, gj = i, j
    
    while not sque.empty():
        i, j = sque.get()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if field[ni][nj] != '#' and sdist[ni][nj] > sdist[i][j] + 1:
                    sdist[ni][nj] = sdist[i][j] + 1
                    sque.put((ni, nj))
    
    while not pque.empty():
        i, j = pque.get()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if field[ni][nj] != '#' and pdist[ni][nj] > pdist[i][j] + 1 and pdist[i][j] + 1 < sdist[ni][nj]:
                    pdist[ni][nj] = pdist[i][j] + 1
                    pque.put((ni, nj))
    
    return pdist[gi][gj] < 1000