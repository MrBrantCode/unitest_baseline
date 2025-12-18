"""
QUESTION:
Given is a tree T with N vertices. The i-th edge connects Vertex A_i and B_i (1 \leq A_i,B_i \leq N).
Now, each vertex is painted black with probability 1/2 and white with probability 1/2, which is chosen independently from other vertices. Then, let S be the smallest subtree (connected subgraph) of T containing all the vertices painted black. (If no vertex is painted black, S is the empty graph.)
Let the holeyness of S be the number of white vertices contained in S. Find the expected holeyness of S.
Since the answer is a rational number, we ask you to print it \bmod 10^9+7, as described in Notes.

-----Notes-----
When you print a rational number, first write it as a fraction \frac{y}{x}, where x, y are integers, and x is not divisible by 10^9 + 7
(under the constraints of the problem, such representation is always possible).
Then, you need to print the only integer z between 0 and 10^9 + 6, inclusive, that satisfies xz \equiv y \pmod{10^9 + 7}.

-----Constraints-----
 - 2 \leq N \leq 2 \times 10^5
 - 1 \leq A_i,B_i \leq N
 - The given graph is a tree.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 B_1
:
A_{N-1} B_{N-1}

-----Output-----
Print the expected holeyness of S, \bmod 10^9+7.

-----Sample Input-----
3
1 2
2 3

-----Sample Output-----
125000001

If the vertices 1, 2, 3 are painted black, white, black, respectively, the holeyness of S is 1.
Otherwise, the holeyness is 0, so the expected holeyness is 1/8.
Since 8 \times 125000001 \equiv 1 \pmod{10^9+7}, we should print 125000001.
"""

def calculate_expected_holeyness(n, edges):
    mod = 10**9 + 7
    
    # Create adjacency list for the tree
    ki = [[] for _ in range(n)]
    for (a, b) in edges:
        ki[a - 1].append(b - 1)
        ki[b - 1].append(a - 1)
    
    # Precompute powers of 2 modulo mod
    n2 = [1]
    for i in range(n):
        n2.append(n2[-1] * 2 % mod)
    
    ans = 0
    
    def dfs1(v, p):
        nonlocal ans
        ret = 0
        ans += n2[n - 1] - 1
        for nv in ki[v]:
            if nv == p:
                continue
            x = dfs1(nv, v)
            ans -= n2[x] - 1
            ans -= n2[n - x] - 1
            ret += x
        ans %= mod
        return ret + 1
    
    dfs1(0, -1)
    
    allpat = pow(2, n, mod)
    ans *= pow(allpat, mod - 2, mod)
    return ans % mod