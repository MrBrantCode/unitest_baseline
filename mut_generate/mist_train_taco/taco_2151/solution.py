"""
QUESTION:
problem

Dimension exists from $ 1 $ dimension to $ N $ dimension. AOR Ika can move between dimensions. Specifically, when AOR Ika is in the $ i $ dimension, she can move freely to the $ j $ dimension ($ i> j $), but in the $ k $ dimension ($ i <k $). You need to use magic to move to.

AOR Ika can use $ M $ types of magic and is numbered $ 1, 2, \ dots, M $. The $ i $ th magic allows you to move from the $ a_i $ dimension to the $ b_i $ dimension. This can only be used when you are in the $ a_i $ dimension.

When you go to the $ i $ dimension, you will receive a dimension-specific "curse of dimensionality". AOR Ika takes $ d_i $ damage due to the "curse of dimensionality" of the $ i $ dimension. If you receive the "curse of dimensionality" of the $ i $ dimension, you will not receive the "curse of dimensionality" of the $ j $ dimension ($ i> j $) forever.

Find the minimum total damage inflicted when AOR Ika moves from the $ s $ dimension to the $ t $ dimension. However, AOR Ika-chan has already received the "curse of dimensionality" of the $ s $ dimension, and we will not consider the damage. Also, AOR Ika is guaranteed to be able to go to the $ t $ dimension.



output

Output the minimum value of the total damage received by AOR Ika-chan. Also, output a line break at the end.

Example

Input

3 1 2 3
1 2 3
1 3


Output

3
"""

import heapq

def minimum_damage(N, M, s, t, d, magic):
    INF = 2147483647
    
    # Convert s and t to 0-based index
    s -= 1
    t -= 1
    
    # Initialize the adjacency list for dimensions
    to = [[] for _ in range(N)]
    for (a, b) in magic:
        to[a - 1].append(b - 1)
    
    # Dijkstra's algorithm to find the minimum damage path
    dist = [INF] * N
    Q = []
    dist[s] = 0
    heapq.heappush(Q, (0, s))
    
    while Q:
        (current_damage, current_dimension) = heapq.heappop(Q)
        if current_dimension == t:
            break
        if dist[current_dimension] < current_damage:
            continue
        for next_dimension in to[current_dimension]:
            next_damage = current_damage
            if next_dimension > current_dimension:
                next_damage += d[next_dimension]
            if dist[next_dimension] > next_damage:
                dist[next_dimension] = next_damage
                heapq.heappush(Q, (next_damage, next_dimension))
    
    return dist[t]