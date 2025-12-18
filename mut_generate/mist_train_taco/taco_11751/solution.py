"""
QUESTION:
## Task

You are at position [0, 0] in maze NxN and you can **only** move in one of the four cardinal directions (i.e. North, East, South, West).  Return `true` if you can reach position [N-1, N-1] or `false` otherwise.

Empty positions are marked `.`. Walls are marked `W`. Start and exit positions are empty in all test cases.

## Path Finder Series:
-       [#1: can you reach the exit?](https://www.codewars.com/kata/5765870e190b1472ec0022a2)
-       [#2: shortest path](https://www.codewars.com/kata/57658bfa28ed87ecfa00058a)
-       [#3: the Alpinist](https://www.codewars.com/kata/576986639772456f6f00030c)
-       [#4: where are you?](https://www.codewars.com/kata/5a0573c446d8435b8e00009f)
-       [#5: there's someone here](https://www.codewars.com/kata/5a05969cba2a14e541000129)
"""

def can_reach_exit(maze):
    matrix = list(map(list, maze.splitlines()))
    stack = [[0, 0]]
    length = len(matrix)
    
    while stack:
        x, y = stack.pop()
        if matrix[x][y] == '.':
            matrix[x][y] = 'x'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < length and 0 <= ny < length:
                    stack.append([nx, ny])
    
    return matrix[length - 1][length - 1] == 'x'