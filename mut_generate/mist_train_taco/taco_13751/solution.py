"""
QUESTION:
Chef and his mother are going travelling. Chef's world consists of $N$ cities (numbered $1$ through $N$) connected by $N-1$ bidirectional roads such that each city can be reached from any other city using roads. For each city, we know its age — the number of years elapsed since the foundation of the city; let's denote the age of city $i$ by $a_i$.
First of all, Chef and his mother have to decide what city they should visit first. Suppose that Chef chooses a city $c_c$ and his mother chooses a (not necessarily different) city $c_m$. The difference of their choices is the number of different bits in the binary representations of $a_{c_c}$ and $a_{c_m}$.
Chef will not argue with his mother if the parity of this difference is not equal to the parity of the length of the shortest path between cities $c_c$ and $c_m$ (the number of roads on the shortest path between them). Find the number of ways to choose the cities $c_c$ and $c_m$ such that Chef avoids quarreling with his mother.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$. 
- Each of the following $N-1$ lines contains two space-separated integers $A$ and $B$ denoting a road between cities $A$ and $B$.
- The last line contains $N$ space-separated integers $a_1, a_2, \dots, a_N$.

-----Output-----
For each test case, print a single line containing one integer — the number of valid pairs $c_c, c_m$.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le A, B \le N$
- $0 \le a_i \le 10^9$ for each valid $i$

-----Sample Input-----
1
3
1 2
1 3
1 2 3

-----Sample Output-----
2

-----Explanation-----
Example case 1: The two possible choices are $c_c=2, c_m=3$ (their binary representations differ by one bit, the shortest path has length $2$) and $c_c=1, c_m=2$ (there are two different bits in their binary representations and the shortest path has length $1$).
"""

def count_valid_city_pairs(N, roads, ages):
    import sys
    sys.setrecursionlimit(10 ** 6)
    
    # Create the graph
    g = [[] for _ in range(N + 1)]
    for (u, v) in roads:
        g[u].append(v)
        g[v].append(u)
    
    # Calculate the parity of the number of 1s in the binary representation of each age
    A = [None] + [bin(age).count('1') % 2 for age in ages]
    
    # Counters for different combinations of parity and depth
    cnt = [0] * 4
    
    # Depth-First Search to populate the counters
    def dfs(u, p, d):
        cnt[A[u] << 1 | d] += 1
        for v in g[u]:
            if v != p:
                dfs(v, u, d ^ 1)
    
    dfs(1, 1, 0)
    
    # Calculate the number of valid pairs
    ans = 0
    for m in range(16):
        (p0, p1, d0, d1) = (m & 1, m >> 1 & 1, m >> 2 & 1, m >> 3 & 1)
        if p0 ^ p1 ^ d0 ^ d1:
            ans += cnt[p0 << 1 | d0] * cnt[p1 << 1 | d1]
    
    return ans // 2