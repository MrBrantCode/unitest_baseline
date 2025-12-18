"""
QUESTION:
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.
We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.
For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.
 

Example 1:
Input: ["@.a.#","###.#","b.A.B"]
Output: 8


Example 2:
Input: ["@..aA","..B#.","....b"]
Output: 6


 
Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""

import heapq
from collections import deque, defaultdict
from typing import List

def shortest_path_all_keys(grid: List[str]) -> int:
    (m, n) = (len(grid), len(grid[0]))
    key_lock_loc = {ch: (i, j) for (i, row) in enumerate(grid) for (j, ch) in enumerate(row) if ch not in {'.', '#'}}
    key_cnt = sum((key_lock in ('a', 'b', 'c', 'd', 'e', 'f') for key_lock in key_lock_loc))

    def bfs_from(src):
        (i, j) = key_lock_loc[src]
        seen = defaultdict(lambda : False)
        seen[i, j] = True
        dque = deque([(i, j, 0)])
        dist = {}
        while dque:
            (i, j, d) = dque.popleft()
            ch = grid[i][j]
            if ch != src and ch != '.':
                dist[ch] = d
                continue
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#' or seen[x, y]:
                    continue
                seen[x, y] = True
                dque.append((x, y, d + 1))
        return dist
    
    dists = {key_lock: bfs_from(key_lock) for key_lock in key_lock_loc}
    all_keys_bitmap = 2 ** key_cnt - 1
    hq = [(0, '@', 0)]
    final_dist = defaultdict(lambda : float('inf'))
    final_dist['@', 0] = 0
    
    while hq:
        (d, ch, keys_bitmap) = heapq.heappop(hq)
        if final_dist[ch, keys_bitmap] < d:
            continue
        if keys_bitmap == all_keys_bitmap:
            return d
        for (next_key_lock, d2) in list(dists[ch].items()):
            keys_bitmap2 = keys_bitmap
            if next_key_lock.islower():
                keys_bitmap2 |= 1 << ord(next_key_lock) - ord('a')
            elif next_key_lock.isupper():
                if not keys_bitmap & 1 << ord(next_key_lock) - ord('A'):
                    continue
            if d + d2 < final_dist[next_key_lock, keys_bitmap2]:
                final_dist[next_key_lock, keys_bitmap2] = d + d2
                heapq.heappush(hq, (d + d2, next_key_lock, keys_bitmap2))
    
    return -1