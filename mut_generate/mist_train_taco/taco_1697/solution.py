"""
QUESTION:
Vietnamese and Bengali as well.
An $N$-bonacci sequence is an infinite sequence $F_1, F_2, \ldots$ such that for each integer $i > N$, $F_i$ is calculated as $f(F_{i-1}, F_{i-2}, \ldots, F_{i-N})$, where $f$ is some function. A XOR $N$-bonacci sequence is an $N$-bonacci sequence for which $f(F_{i-1}, F_{i-2}, \ldots, F_{i-N}) = F_{i-1} \oplus F_{i−2} \oplus \ldots \oplus F_{i−N}$, where $\oplus$ denotes the bitwise XOR operation.
Recently, Chef has found an interesting sequence $S_1, S_2, \ldots$, which is obtained from prefix XORs of a XOR $N$-bonacci sequence $F_1, F_2, \ldots$. Formally, for each positive integer $i$, $S_i = F_1 \oplus F_2 \oplus \ldots \oplus F_i$. You are given the first $N$ elements of the sequence $F$, which uniquely determine the entire sequence $S$.
You should answer $Q$ queries. In each query, you are given an index $k$ and you should calculate $S_k$. It is guaranteed that in each query, $S_k$ does not exceed $10^{50}$.

-----Input-----
- The first line of the input contains two space-separated integers $N$ and $Q$.
- The second line contains $N$ space-separated integers $F_1, F_2, \ldots, F_N$.
- The following $Q$ lines describe queries. Each of these lines contains a single integer $k$.

-----Output-----
For each query, print a single line containing one integer $S_k$.

-----Constraints-----
- $1 \le N, Q \le 10^5$
- $0 \le F_i \le 10^9$ for each $i$ such that $1 \le i \le N$
- $1 \le k \le 10^9$

-----Example Input-----
3 4
0 1 2
7
2
5
1000000000

-----Example Output-----
3
1
0
0
"""

def calculate_xor_n_bonacci_prefix(N, Q, F, queries):
    # Initialize the list to store prefix XOR results
    l = [0, F[0]]
    
    # Calculate the prefix XOR for the first N elements
    for i in range(1, N):
        l.append(l[-1] ^ F[i])
    
    # Append an additional 0 to handle cases where k % (N + 1) == 0
    l.append(0)
    
    # Prepare the results for each query
    results = []
    for k in queries:
        results.append(l[k % (N + 1)])
    
    return results