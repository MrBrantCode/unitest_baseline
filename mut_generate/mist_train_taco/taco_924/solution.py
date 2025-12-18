"""
QUESTION:
Let $A$ be an array of $N$ elements and let us define beauty of array as (consider 1 based indexing)

long long int beauty(int N, int A[]){
long long int val = 0;
for(int i = 1; i < N; i++){
for(int j = i + 1; j ≤ N; j++){
if(a[i] < a[j]){val++;}
else{val--;}
}
}
return val;
}

Let $G$ be a tree with $N$ nodes numbered from $1$ to $N$ rooted at node $1$. Find the Expected Beauty of all the valid $BFS(Breadth First Search)$ of $G$.
Expected beauty of a $BFS$ can be calculated using above function considering visiting order as elements of the array.

------ Input: ------

First line will contain $N$, the number of nodes. 
This will be followed by $N - 1$ lines each containing two space-separated integers $a$, $b$ denoting that their is an edge between nodes $a$ and $b$.

------ Output: ------

On a single line, print a real number, the answer to the problem. Your answer will be considered correct if its absolute or relative error does not exceed ${10}^{-6}$. Formally, if your answer is $a$ and the jury's answer is $b$, your answer will be accepted if $\frac{|a-b|}{max(1,b)} ≤ {10}^{-6}$.

------ Constraints: ------
$1 ≤ N ≤ 2 * 10^{5}$

------ Sample Input ------

3
1 2
1 3

------ Expected Output ------
2.000000

------ Explanation: ------
Valid BFSs are 1 2 3 — beauty = $3$; and 1 3 2 — beauty = $1$.

So, Expected Beauty is equal to $\frac{1}{2} * 3 + \frac{1}{2} * 1 = 2.000$.
"""

def calculate_expected_beauty(n, edges):
    class FenwickTree:
        def __init__(self, n):
            self.BITTree = [0] * (n + 1)
            self.size = n

        def getsum(self, i):
            s = 0
            i = i + 1
            while i > 0:
                s += self.BITTree[i]
                i -= i & -i
            return s

        def query(self, l, r):
            return self.getsum(r) - self.getsum(l - 1)

        def update(self, i, v):
            i += 1
            while i <= self.size:
                self.BITTree[i] += v
                i += i & -i

    def dfs(p, prev, lvl):
        level[lvl].append(p)
        for i in child[p]:
            if i == prev:
                continue
            dfs(i, p, lvl + 1)

    def answer():
        f = FenwickTree(n + 1)
        ans = 0
        for i in range(n):
            for j in level[i]:
                ans += f.query(1, j) - f.query(j, n)
            for j in level[i]:
                f.update(j, 1)
        return ans

    child = [[] for _ in range(n + 1)]
    for u, v in edges:
        child[u].append(v)
        child[v].append(u)

    level = [[] for _ in range(n)]
    dfs(1, -1, 0)

    return answer()