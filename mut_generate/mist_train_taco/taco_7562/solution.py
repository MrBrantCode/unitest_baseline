"""
QUESTION:
Taro made a sugoroku so that everyone can play at the children's association event. In order to make the game interesting, I wrote instructions such as "advance 6" and "back 5" in some of the sugoroku squares other than "Furidashi" and "Agari". Turn the roulette wheel to advance as many times as you can, and if an instruction is written on the stopped square, move according to that instruction. However, it does not follow the instructions of the squares that proceeded according to the instructions.

Roulette shall be able to give a number between 1 and a certain number with equal probability. Also, if you get a larger number than you reach "Agari", or if you follow the instructions and you go beyond "Agari", you will move to "Agari". If you follow the instructions and return before "Furidashi", you will return to "Furidashi".

<image>


However, depending on the instructions of the roulette wheel and the square, it may not be possible to reach the "rise". For example, let's say you made a sugoroku like the one shown in the figure. If you use a roulette wheel that only gives 1 and 2, you can go to "Agari" if you come out in the order of 1 and 2, but if you get 2 first, you will not be able to reach "Agari" forever no matter what comes out. Taro didn't know that and wrote instructions in various squares.

Therefore, on behalf of Taro, please create a program to determine whether or not you may not be able to reach the "rise" depending on the instructions of the roulette and the square.



input

The input consists of multiple datasets. The end of the input is indicated by a single zero line. Each dataset is given in the following format.


max
n
d1
d2
..
..
..
dn


The first line gives the maximum number of roulette wheels max (2 ≤ max ≤ 250), and the second line gives the number of cells other than "starting" and "rising" n (2 ≤ n ≤ 250). .. The next n lines are given the number di (-n ≤ di ≤ n) that represents the indication for each cell. When di is zero, it means that no instruction is written, when it is a positive number, it means | di | forward instruction, and when it is negative, it means | di | back instruction (where | x | is x). Represents an absolute value). All values ​​entered are integers.

The number of datasets does not exceed 100.

output

The judgment result is output to one line for each data set. Depending on the instructions of the roulette and the square, if it may not be possible to reach the "go up", "NG" is output, otherwise "OK" is output.

Example

Input

3
3
-2
1
0
2
4
2
0
-1
-2
2
2
-2
-2
0


Output

OK
NG
NG
"""

def can_reach_goal(max_roulette, n, instructions):
    # Add dummy instructions for "Furidashi" and "Agari"
    ds = [0] + instructions + [0]
    
    # Initialize graph and reverse graph
    g = [[] for _ in range(n + 2)]
    rg = [[] for _ in range(n + 2)]
    
    # Build the graph and reverse graph
    for i in range(n + 2):
        for j in range(min(n + 1, i + 1), min(n + 1, i + max_roulette) + 1):
            j = max(0, min(n + 1, j + ds[j]))
            g[i].append(j)
            rg[j].append(i)
    
    # Depth-first search function
    def dfs(graph, visited, i):
        visited[i] = True
        for j in graph[i]:
            if not visited[j]:
                dfs(graph, visited, j)
    
    # Initialize visited arrays for both graphs
    visited_g = [False] * (n + 2)
    visited_rg = [False] * (n + 2)
    
    # Perform DFS on both graphs
    dfs(g, visited_g, 0)
    dfs(rg, visited_rg, n + 1)
    
    # Check if there's any node reachable from "Furidashi" but not from "Agari"
    if any((b and not rb) for b, rb in zip(visited_g, visited_rg)):
        return 'NG'
    else:
        return 'OK'