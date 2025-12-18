"""
QUESTION:
You've gotten an n × m sheet of squared paper. Some of its squares are painted. Let's mark the set of all painted squares as A. Set A is connected. Your task is to find the minimum number of squares that we can delete from set A to make it not connected.

A set of painted squares is called connected, if for every two squares a and b from this set there is a sequence of squares from the set, beginning in a and ending in b, such that in this sequence any square, except for the last one, shares a common side with the square that follows next in the sequence. An empty set and a set consisting of exactly one square are connected by definition.

Input

The first input line contains two space-separated integers n and m (1 ≤ n, m ≤ 50) — the sizes of the sheet of paper. 

Each of the next n lines contains m characters — the description of the sheet of paper: the j-th character of the i-th line equals either "#", if the corresponding square is painted (belongs to set A), or equals "." if the corresponding square is not painted (does not belong to set A). It is guaranteed that the set of all painted squares A is connected and isn't empty.

Output

On the first line print the minimum number of squares that need to be deleted to make set A not connected. If it is impossible, print -1. 

Examples

Input

5 4
####
#..#
#..#
#..#
####


Output

2


Input

5 5
#####
#...#
#####
#...#
#####


Output

2

Note

In the first sample you can delete any two squares that do not share a side. After that the set of painted squares is not connected anymore.

The note to the second sample is shown on the figure below. To the left there is a picture of the initial set of squares. To the right there is a set with deleted squares. The deleted squares are marked with crosses. 

<image>
"""

def min_squares_to_disconnect(n, m, paper):
    p = []
    s = {}
    x = 0
    
    # Build the graph of connected painted squares
    for i in range(n):
        for j in range(m):
            if paper[i][j] != '#':
                continue
            s[(i, j)] = x
            p.append([])
            if (i, j - 1) in s:
                p[x].append(x - 1)
                p[x - 1].append(x)
            if (i - 1, j) in s:
                y = s[(i - 1, j)]
                p[x].append(y)
                p[y].append(x)
            x += 1
    
    k = len(p)
    
    # If there are less than 3 painted squares, it's impossible to disconnect them
    if k < 3:
        return -1
    
    # Try removing each node and check if the graph becomes disconnected
    for j in range(k):
        d = [1] * k
        d[j] = 0
        stack = [p[j][0]]
        while stack:
            node = stack.pop()
            if not d[node]:
                continue
            d[node] = 0
            for neighbor in p[node]:
                if d[neighbor]:
                    stack.append(neighbor)
        if 1 in d:
            return 1
    
    # If removing any single node doesn't work, return 2
    return 2