"""
QUESTION:
The MEX of a set of integers is defined as the smallest non-negative integer that does not belong to this set. For example, $\mathrm{MEX}(\{0,2,3\}) = 1$ and $\mathrm{MEX}(\{1,3\}) = 0$.
Chef has a tree with $N$ nodes (numbered $1$ through $N$). The tree is rooted at node $1$. Chef wants to assign a non-negative integer to each node in such a way that each integer between $0$ and $N-1$ (inclusive) is assigned to exactly one node.
For each node $u$, consider the integers assigned to the nodes in the subtree of $u$ (including $u$); let $a_u$ denote the MEX of these integers. Chef wants $a_1 + a_2 + \ldots + a_N$ to be as large as possible. Find the maximum possible value of this sum.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N-1$ space-separated integers $p_1, p_2, \ldots, p_{N-1}$. For each valid $i$, the node $p_i$ is the parent of the node $i+1$.

-----Output-----
For each test case, print a single line containing one integer ― the maximum sum of subtree MEX-s which can be obtained if you assign the weights optimally.

-----Constraints-----
- $1 \le T \le 5$
- $2 \le N \le 10^5$
- $1 \le p_i < i$ for each valid $i$

-----Subtasks-----
Subtask #1 (100 points): original constraints

-----Example Input-----
2
3
1 1
5
1 1 2 2

-----Example Output-----
4
9
"""

def calculate_max_subtree_mex_sum(n, parents):
    def ans(dic, n):
        if dic.get(n) is not None:
            b = []
            for a in dic[n]:
                b.append(ans(dic, a))
            mx = 0
            node = 0
            for a in b:
                if a[0] > mx:
                    mx = a[0]
                node += a[1]
            node += len(dic[n])
            return (mx + node + 1, node)
        else:
            return (1, 0)
    
    dic = {}
    for j in range(1, n):
        temp = parents[j - 1]
        if dic.get(temp) is None:
            dic[temp] = [j + 1]
        else:
            dic[temp].append(j + 1)
    
    anss = ans(dic, 1)
    return anss[0]