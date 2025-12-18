"""
QUESTION:
The goal of the 8 puzzle problem is to complete pieces on $3 \times 3$ cells where one of the cells is empty space.

In this problem, the space is represented by 0 and pieces are represented by integers from 1 to 8 as shown below.


1 3 0
4 2 5
7 8 6


You can move a piece toward the empty space at one step. Your goal is to make the pieces the following configuration in the shortest move (fewest steps).


1 2 3
4 5 6
7 8 0


Write a program which reads an initial state of the puzzle and prints the fewest steps to solve the puzzle.

Constraints

* There is a solution.

Input

The $3 \times 3$ integers denoting the pieces or space are given.

Output

Print the fewest steps in a line.

Example

Input

1 3 0
4 2 5
7 8 6


Output

4
"""

import collections

def solve_8_puzzle(initial_state):
    SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    neighbor = ((1, 3), (0, 2, 4), (1, 5), (0, 4, 6), (1, 3, 5, 7), (2, 4, 8), (3, 7), (4, 6, 8), (5, 7))
    
    dist = dict()
    que = collections.deque()
    initial_state = tuple(initial_state)
    que.append((initial_state, initial_state.index(0)))
    dist[initial_state] = 0
    
    while que:
        (c, idx_0) = que.popleft()
        if c == SOLVED:
            return dist[SOLVED]
        for i in neighbor[idx_0]:
            c_l = list(c)
            (c_l[idx_0], c_l[i]) = (c_l[i], c_l[idx_0])
            n = tuple(c_l)
            if n not in dist:
                que.append((n, i))
                dist[n] = dist[c] + 1
    
    return dist[SOLVED]