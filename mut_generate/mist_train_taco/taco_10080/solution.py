"""
QUESTION:
The zombie apocalypse is here and Chef is stuck at an old construction site. The site is surrounded by walls on three sides. On the fourth side is a fence where $N$ zombies are standing in a row. The zombies are numbered from $1$ to $N$ from left to right. Zombie $i$ has $Z_{i}$ health points initially.

Luckily there are $M$ cranes Chef has access to. The $i^{th}$ crane carries $K_{i}$ construction beams. Chef can drop any number $≥ 0$ and $≤ K_{i}$ of these beams from crane $i$ and they will hit all zombies whose numbers lie between $L_{i}$ to $R_{i}$ both inclusive. A single beam decreases the health of all zombies it hits by $1$ point. If a zombie's health equals $0$ after being hit it is considered dead.

Can Chef kill all the zombies using the beams? If yes, what is the minimum number of beams that Chef has to drop to achieve this?

Warning: Large I/O, it is advisable to use fast I/O methods.

------  Input: ------
The first line contains $T$, number of testcases. 
The first line of each test case contains two integers $N$ and $M$.
The second line of each test case contains $N$ integers $Z_{1}, Z_{2}, ..., Z_{N}$.
$M$ lines follow. The $i^{th}$ line contains $3$ integers $L_{i}$, $R_{i}$ and $K_{i}$.

------  Output: ------
For each test case, if it is possible for Chef to kill all the zombies print a single line containing "YES" followed by the minimum number of beams he needs to drop. If it is impossible, print "NO" instead. (Note that the judge is case-sensitive)

------  Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ N, M ≤ 10^{5}$
Sum of $N$ over all test cases $≤ 3 \cdot 10^{5}$
Sum of $M$ over all test cases $≤ 3 \cdot 10^{5}$
$1 ≤ Z_{i} ≤ 10^{9}$
$1 ≤ L_{i} ≤ R_{i} ≤ N$
$1 ≤ K_{i} ≤ 10^{9}$

------  Sample Input: ------
2
5 5
1 2 3 4 5
1 2 3
1 5 1
2 4 3
3 5 3
4 5 3
3 2
2 5 2
1 2 2
2 3 2

------  Sample Output: ------
YES 6
NO
	
------  Explanation: ------
Case 1: One possible way is for Chef to drop the only beam from crane 2, 1 beam from crane 3, 1 beam from crane 4 and all 3 beams from crane 5.
Case 2: Zombie 1 and 3 can be killed but zombie 2 remains at health 1 even if all the beams are dropped.
"""

import heapq

def can_chef_kill_all_zombies(T, test_cases):
    results = []
    
    for case in test_cases:
        N, M, Z, cranes = case
        C = [[] for _ in range(N)]
        
        for L, R, K in cranes:
            C[L - 1].append((R - 1, K))
        
        D = [0] * (N + 1)
        heap = []
        ans = dmg = 0
        
        for i in range(N):
            dmg -= D[i]
            for (R, K) in C[i]:
                heapq.heappush(heap, (-R, K))
            Z[i] -= dmg
            while Z[i] > 0:
                if not heap or -heap[0][0] < i:
                    ans = -1
                    break
                (R, K) = heapq.heappop(heap)
                R = -R
                d = min(K, Z[i])
                Z[i] -= d
                K -= d
                ans += d
                dmg += d
                D[R + 1] += d
                if K:
                    heapq.heappush(heap, (-R, K))
            if ans == -1:
                break
        
        if ans == -1:
            results.append('NO')
        else:
            results.append(f'YES {ans}')
    
    return results