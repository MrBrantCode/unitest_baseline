"""
QUESTION:
You are given a tree with N vertices. The vertices are numbered 0 through N-1, and the edges are numbered 1 through N-1. Edge i connects Vertex x_i and y_i, and has a value a_i. You can perform the following operation any number of times:

* Choose a simple path and a non-negative integer x, then for each edge e that belongs to the path, change a_e by executing a_e ← a_e ⊕ x (⊕ denotes XOR).



Your objective is to have a_e = 0 for all edges e. Find the minimum number of operations required to achieve it.

Constraints

* 2 ≤ N ≤ 10^5
* 0 ≤ x_i,y_i ≤ N-1
* 0 ≤ a_i ≤ 15
* The given graph is a tree.
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N
x_1 y_1 a_1
x_2 y_2 a_2
:
x_{N-1} y_{N-1} a_{N-1}


Output

Find the minimum number of operations required to achieve the objective.

Examples

Input

5
0 1 1
0 2 3
0 3 6
3 4 4


Output

3


Input

2
1 0 0


Output

0
"""

from collections import Counter
from functools import reduce
from itertools import combinations
from operator import xor

def min_operations_to_zero_xor(n, edges):
    nodes = [0] * n
    
    for x, y, a in edges:
        nodes[x] ^= a
        nodes[y] ^= a
    
    c = Counter(nodes)
    ans = 0
    remains = set()
    
    for i, v in c.items():
        if i == 0:
            continue
        ans += v // 2
        if v % 2:
            remains.add(i)
    
    for r in (3, 4, 5):
        while True:
            for ns in combinations(remains, r):
                if reduce(xor, ns) == 0:
                    remains.difference_update(ns)
                    ans += r - 1
                    break
            else:
                break
    
    return ans