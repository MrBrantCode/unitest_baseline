"""
QUESTION:
While Farmer John rebuilds his farm in an unfamiliar portion of Bovinia, Bessie is out trying some alternative jobs. In her new gig as a reporter, Bessie needs to know about programming competition results as quickly as possible. When she covers the 2016 Robot Rap Battle Tournament, she notices that all of the robots operate under deterministic algorithms. In particular, robot i will beat robot j if and only if robot i has a higher skill level than robot j. And if robot i beats robot j and robot j beats robot k, then robot i will beat robot k. Since rapping is such a subtle art, two robots can never have the same skill level.

Given the results of the rap battles in the order in which they were played, determine the minimum number of first rap battles that needed to take place before Bessie could order all of the robots by skill level.


-----Input-----

The first line of the input consists of two integers, the number of robots n (2 ≤ n ≤ 100 000) and the number of rap battles m ($1 \leq m \leq \operatorname{min}(100000, \frac{n(n - 1)}{2})$).

The next m lines describe the results of the rap battles in the order they took place. Each consists of two integers u_{i} and v_{i} (1 ≤ u_{i}, v_{i} ≤ n, u_{i} ≠ v_{i}), indicating that robot u_{i} beat robot v_{i} in the i-th rap battle. No two rap battles involve the same pair of robots.

It is guaranteed that at least one ordering of the robots satisfies all m relations.


-----Output-----

Print the minimum k such that the ordering of the robots by skill level is uniquely defined by the first k rap battles. If there exists more than one ordering that satisfies all m relations, output -1.


-----Examples-----
Input
4 5
2 1
1 3
2 3
4 2
4 3

Output
4

Input
3 2
1 2
3 2

Output
-1



-----Note-----

In the first sample, the robots from strongest to weakest must be (4, 2, 1, 3), which Bessie can deduce after knowing the results of the first four rap battles.

In the second sample, both (1, 3, 2) and (3, 1, 2) are possible orderings of the robots from strongest to weakest after both rap battles.
"""

def minimum_rap_battles_for_ordering(n, m, edges):
    lo = 0
    hi = m
    curr_k = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        can_do = True
        adj_list = {x: [] for x in range(n)}
        in_degree = [0] * n
        
        for ed in range(min(mid, len(edges))):
            edge = edges[ed]
            adj_list[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        
        candidates = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                candidates.append(i)
        
        res = []
        while candidates:
            ele = candidates.pop(0)
            if len(candidates) > 0:
                can_do = False
                break
            res.append(ele)
            for i in adj_list[ele]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    candidates.append(i)
        
        if len(res) < n:
            can_do = False
        
        if can_do:
            curr_k = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return curr_k