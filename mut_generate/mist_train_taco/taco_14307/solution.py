"""
QUESTION:
## Task

You are at position `[0, 0]` in maze NxN and you can **only** move in one of the four cardinal directions (i.e. North, East, South, West). Return the minimal number of steps to exit position `[N-1, N-1]` *if* it is possible to reach the exit from the starting position.  Otherwise, return `false` in **JavaScript**/**Python** and `-1` in **C++**/**C#**/**Java**.

Empty positions are marked `.`.  Walls are marked `W`.  Start and exit positions are guaranteed to be empty in all test cases.

## Path Finder Series:

-       [#1: can you reach the exit?](https://www.codewars.com/kata/5765870e190b1472ec0022a2)
-       [#2: shortest path](https://www.codewars.com/kata/57658bfa28ed87ecfa00058a)
-       [#3: the Alpinist](https://www.codewars.com/kata/576986639772456f6f00030c)
-       [#4: where are you?](https://www.codewars.com/kata/5a0573c446d8435b8e00009f)
-       [#5: there's someone here](https://www.codewars.com/kata/5a05969cba2a14e541000129)
"""

def find_shortest_path(maze):
    lst = maze.split('\n')
    (X, Y) = (len(lst) - 1, len(lst[0]) - 1)
    seen = {(x, y) for (x, row) in enumerate(lst) for (y, c) in enumerate(row) if c == 'W'} | {(0, 0)}
    (end, bag, turn) = ((X, Y), {(0, 0)}, 0)
    while bag and end not in bag:
        bag = {(a, b) for (a, b) in {(x + dx, y + dy) for (x, y) in bag for (dx, dy) in ((0, 1), (0, -1), (1, 0), (-1, 0))} if 0 <= a <= X and 0 <= b <= Y} - seen
        seen |= bag
        turn += 1
    return bool(bag) and turn