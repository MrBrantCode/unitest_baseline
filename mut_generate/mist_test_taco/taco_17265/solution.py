"""
QUESTION:
We have a tree with N vertices. The vertices are numbered 1 to N, and the i-th edge connects Vertex a_i and Vertex b_i.

Takahashi loves the number 3. He is seeking a permutation p_1, p_2, \ldots , p_N of integers from 1 to N satisfying the following condition:

* For every pair of vertices (i, j), if the distance between Vertex i and Vertex j is 3, the sum or product of p_i and p_j is a multiple of 3.



Here the distance between Vertex i and Vertex j is the number of edges contained in the shortest path from Vertex i to Vertex j.

Help Takahashi by finding a permutation that satisfies the condition.

Constraints

* 2\leq N\leq 2\times 10^5
* 1\leq a_i, b_i \leq N
* The given graph is a tree.

Input

Input is given from Standard Input in the following format:


N
a_1 b_1
a_2 b_2
\vdots
a_{N-1} b_{N-1}


Output

If no permutation satisfies the condition, print `-1`.

Otherwise, print a permutation satisfying the condition, with space in between. If there are multiple solutions, you can print any of them.

Example

Input

5
1 2
1 3
3 4
3 5


Output

1 2 5 4 3
"""

def find_permutation_for_takahashi(n, edges):
    import sys
    sys.setrecursionlimit(10 ** 6)
    
    edge = [[] for _ in range(n)]
    ans = [-1] * n
    odd = []
    even = []
    nums = [[], [], []]
    
    for i in range(1, n + 1):
        nums[i % 3].append(i)
    
    def dfs(x, last=-1, d=0):
        if d % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
        for nxt in edge[x]:
            if nxt == last:
                continue
            dfs(nxt, x, d + 1)
    
    for a, b in edges:
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    
    dfs(0)
    
    zerocnt = len(nums[0])
    
    if len(even) <= zerocnt:
        for even_node in even:
            ans[even_node] = nums[0].pop()
        rest = nums[0] + nums[1] + nums[2]
        for odd_node in odd:
            ans[odd_node] = rest.pop()
    elif len(odd) <= zerocnt:
        for odd_node in odd:
            ans[odd_node] = nums[0].pop()
        rest = nums[0] + nums[1] + nums[2]
        for even_node in even:
            ans[even_node] = rest.pop()
    else:
        for num in nums[1]:
            ans[even.pop()] = num
        for num in nums[2]:
            ans[odd.pop()] = num
        rest = nums[0]
        for even_node in even:
            ans[even_node] = rest.pop()
        for odd_node in odd:
            ans[odd_node] = rest.pop()
    
    return ans if -1 not in ans else -1