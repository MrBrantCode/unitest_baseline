"""
QUESTION:
Whereas humans nowadays read fewer and fewer books on paper, book readership among marmots has surged. Heidi has expanded the library and is now serving longer request sequences.


-----Input-----

Same as the easy version, but the limits have changed: 1 ≤ n, k ≤ 400 000.


-----Output-----

Same as the easy version.


-----Examples-----
Input
4 100
1 2 2 1

Output
2

Input
4 1
1 2 2 1

Output
3

Input
4 2
1 2 3 1

Output
3
"""

from collections import deque, defaultdict
from heapq import heappush, heappop

def calculate_minimum_swaps(n, k, A):
    dic = defaultdict(deque)
    for (i, a) in enumerate(A):
        dic[a].append(i)
    
    hp = []
    S = set()
    ans = 0
    
    for (i, a) in enumerate(A):
        dic[a].popleft()
        if a not in S:
            if len(S) < k:
                S.add(a)
                ans += 1
            else:
                idx = heappop(hp)[1]
                S.discard(idx)
                S.add(a)
                ans += 1
        if dic[a]:
            heappush(hp, (-dic[a][0], a))
        else:
            heappush(hp, (float('-inf'), a))
    
    return ans