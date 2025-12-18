"""
QUESTION:
There are N islands and M bridges.
The i-th bridge connects the A_i-th and B_i-th islands bidirectionally.
Initially, we can travel between any two islands using some of these bridges.
However, the results of a survey show that these bridges will all collapse because of aging, in the order from the first bridge to the M-th bridge.
Let the inconvenience be the number of pairs of islands (a, b) (a < b) such that we are no longer able to travel between the a-th and b-th islands using some of the bridges remaining.
For each i (1 \leq i \leq M), find the inconvenience just after the i-th bridge collapses.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 10^5
 - 1 \leq M \leq 10^5
 - 1 \leq A_i < B_i \leq N
 - All pairs (A_i, B_i) are distinct.
 - The inconvenience is initially 0.

-----Input-----
Input is given from Standard Input in the following format:
N M
A_1 B_1
A_2 B_2
\vdots
A_M B_M

-----Output-----
In the order i = 1, 2, ..., M, print the inconvenience just after the i-th bridge collapses.
Note that the answer may not fit into a 32-bit integer type.

-----Sample Input-----
4 5
1 2
3 4
1 3
2 3
1 4

-----Sample Output-----
0
0
4
5
6

For example, when the first to third bridges have collapsed, the inconvenience is 4 since we can no longer travel between the pairs (1, 2), (1, 3), (2, 4) and (3, 4).
"""

class UnionFind:
    def __init__(self, n):
        self.par = [x for x in range(n)]
        self.rank = [1] * n
        self.num = [1] * n

    def root(self, a):
        if self.par[a] == a:
            return a
        parent = self.root(self.par[a])
        self.par[a] = parent
        return parent

    def unite(self, a, b):
        (ra, rb) = (self.root(a), self.root(b))
        out = self.num[ra] * self.num[rb]
        if self.rank[ra] < self.rank[rb]:
            (ra, rb) = (rb, ra)
        self.par[rb] = ra
        self.num[ra] += self.num[rb]
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return out

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def com_num(self, a, b):
        if self.same(a, b):
            return 0
        else:
            return self.unite(a, b)

def calculate_inconvenience(n, m, bridges):
    incon = [0] * (m + 1)
    uf = UnionFind(n)
    
    # Initialize the inconvenience for the state after all bridges have collapsed
    incon[m] = n * (n - 1) // 2
    
    # Calculate inconvenience in reverse order (from last bridge to first)
    for i in range(m - 1, -1, -1):
        (a, b) = bridges[i]
        incon[i] = incon[i + 1] - uf.com_num(a - 1, b - 1)
    
    # Return the inconvenience list excluding the last element (which is the initial state)
    return incon[1:]