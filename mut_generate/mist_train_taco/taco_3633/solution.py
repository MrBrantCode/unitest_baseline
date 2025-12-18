"""
QUESTION:
Boy Valera likes strings. And even more he likes them, when they are identical. That's why in his spare time Valera plays the following game. He takes any two strings, consisting of lower case Latin letters, and tries to make them identical. According to the game rules, with each move Valera can change one arbitrary character Ai in one of the strings into arbitrary character Bi, but he has to pay for every move a particular sum of money, equal to Wi. He is allowed to make as many moves as he needs. Since Valera is a very economical boy and never wastes his money, he asked you, an experienced programmer, to help him answer the question: what minimum amount of money should Valera have to get identical strings. 

Input

The first input line contains two initial non-empty strings s and t, consisting of lower case Latin letters. The length of each string doesn't exceed 105. The following line contains integer n (0 ≤ n ≤ 500) — amount of possible changings. Then follow n lines, each containing characters Ai and Bi (lower case Latin letters) and integer Wi (0 ≤ Wi ≤ 100), saying that it's allowed to change character Ai into character Bi in any of the strings and spend sum of money Wi.

Output

If the answer exists, output the answer to the problem, and the resulting string. Otherwise output -1 in the only line. If the answer is not unique, output any.

Examples

Input

uayd
uxxd
3
a x 8
x y 13
d c 3


Output

21
uxyd


Input

a
b
3
a b 2
a b 3
b a 5


Output

2
b


Input

abc
ab
6
a b 4
a b 7
b a 8
c b 11
c a 3
a c 0


Output

-1
"""

import string
import itertools

def minimum_cost_to_make_identical_strings(s, t, n, changes):
    if len(s) != len(t):
        return -1, None
    
    vertices = string.ascii_lowercase
    g = {c: {c: 0} for c in vertices}
    
    for (u, v, cost) in changes:
        cost = int(cost)
        if v not in g[u] or g[u][v] > cost:
            g[u][v] = cost
    
    for p in vertices:
        for u in vertices:
            if p not in g[u]:
                continue
            for v in vertices:
                if v not in g[p]:
                    continue
                if v not in g[u] or g[u][v] > g[u][p] + g[p][v]:
                    g[u][v] = g[u][p] + g[p][v]
    
    best_costs = {c: {c: 0} for c in vertices}
    best_chars = {c: {c: c} for c in vertices}
    
    for (a, b) in itertools.product(vertices, vertices):
        if a == b:
            continue
        best_cost = None
        best_char = None
        for c in vertices:
            if c in g[a] and c in g[b]:
                if best_cost is None or best_cost > g[a][c] + g[b][c]:
                    best_cost = g[a][c] + g[b][c]
                    best_char = c
        if b in g[a] and (best_cost is None or best_cost > g[a][b]):
            best_cost = g[a][b]
            best_char = b
        if a in g[b] and (best_cost is None or best_cost > g[b][a]):
            best_cost = g[b][a]
            best_char = a
        if best_cost is None:
            continue
        best_costs[a][b] = best_cost
        best_chars[a][b] = best_char
    
    total_cost = 0
    chars = []
    
    for (a, b) in zip(s, t):
        if b not in best_costs[a]:
            return -1, None
        total_cost += best_costs[a][b]
        chars.append(best_chars[a][b])
    
    result_string = ''.join(chars)
    return total_cost, result_string