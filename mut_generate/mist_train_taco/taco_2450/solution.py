"""
QUESTION:
Storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.
The game is represented by a grid of size m x n, where each element is a wall, floor, or a box.
Your task is move the box 'B' to the target position 'T' under the following rules:

Player is represented by character 'S' and can move up, down, left, right in the grid if it is a floor (empy cell).
Floor is represented by character '.' that means free cell to walk.
Wall is represented by character '#' that means obstacle  (impossible to walk there). 
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.
 
Example 1:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.

Example 4:
Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1

 
Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 20
1 <= n <= 20
grid contains only characters '.', '#',  'S' , 'T', or 'B'.
There is only one character 'S', 'B' and 'T' in the grid.
"""

import heapq
import collections

def min_push_box(grid):
    (m, n, g) = (len(grid), len(grid[0]), collections.defaultdict(list))
    for i in range(m):
        for j in range(n):
            g[grid[i][j]] += [complex(i, j)]

    def f(b, s):
        nonlocal time
        time += 1
        boxToTarget = b - target
        return (abs(boxToTarget.real) + abs(boxToTarget.imag) + s, abs(boxToTarget), time)
    
    (player, box, target, time) = (*g['S'], *g['B'], *g['T'], 1)
    floor = {player, box, target, *g['.']}
    alpha = [(f(box, 1), 1, player, box)]
    (directions, visited) = ((1, -1, 1j, -1j), set())
    low = dict.fromkeys(floor, 0)
    dfn = low.copy()
    count = 0
    index = {}

    def tarjan(currIndex, parentIndex):
        nonlocal count
        count += 1
        dfn[currIndex] = low[currIndex] = count
        index[count] = currIndex
        for direction in directions:
            nextIndex = currIndex + direction
            if nextIndex in floor and nextIndex != parentIndex:
                if not low[nextIndex]:
                    tarjan(nextIndex, currIndex)
                low[currIndex] = min(low[currIndex], low[nextIndex])
    
    tarjan(box, -1)
    for currIndex in floor:
        connect = [currIndex]
        while dfn[connect[-1]] != low[connect[-1]]:
            connect.append(index[low[connect[-1]]])
        for w in connect[:-2]:
            low[w] = low[connect[-1]]
    
    if not low[player] * low[target]:
        return -1
    
    while alpha:
        (_, steps, currPlayer, currBox) = heapq.heappop(alpha)
        for direction in directions:
            (nextPlayer, nextBox) = (currBox - direction, currBox + direction)
            if nextBox in floor and nextPlayer in floor and ((nextPlayer, currBox) not in visited) and (low[currPlayer] == low[nextPlayer]):
                if nextBox == target:
                    return steps
                heapq.heappush(alpha, (f(nextBox, steps + 1), steps + 1, currBox, nextBox))
                visited.add((nextPlayer, currBox))
    
    return -1