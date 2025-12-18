"""
QUESTION:
There are $N$ villages numbered $1$ to $N$. The villages are connected through bi-directional paths in between them. The whole network is in the form of a tree. 
Each village has only $1$ fighter but they help each other in times of crisis by sending their fighter to the village in danger through paths along the villages. Defeating a fighter will mean conquering his village. In particular, If village $X$ is under attack, all villages having a path to $X$ will send their fighters for help. 
Naruto wants to conquer all the villages. But he cannot take on so many fighters at the same time so he plans to use  a secret technique with which he can destroy  any $1$ village (along with paths connected to it) in the blink of an eye.  However, it can be used only once. He realized that if he destroys any village, say $X$, the maximum number of fighters he has to fight at once reduces to $W$. He wants $W$ to be as small as possible. Help him find the optimal $X$.
In case of multiple answers, choose the smallest value of $X$.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- First Line contains $N$.
- Next $N - 1$ lines contain $U, V$, denoting a path between village $U$ and $V$. 

-----Output:-----
- For each Test case, print in a new line, optimal $X$ and corresponding value of $W$.

-----Constraints-----
- $1 \leq T \leq 10$
- $3 \leq N \leq 10^5$
- $1 \leq U, V \leq N$ 
- $U != V$ 

-----Sample Input:-----
2
5
1 2
1 3
2 4
3 5
3
1 2
2 3

-----Sample Output:-----
1 2
2 1

-----EXPLANATION:-----
Sample 1:  By destroying village $1$,  The fighters Naruto will be fighting at the same time will be from villages $[2, 4]$ and $[3, 5]$.  For this $W$ = $2$. No other choice can give lesser $W$. Hence $1$ is optimal choice.
"""

def find_optimal_village(n, edges):
    visited = set()
    parents = [-1] * (n + 1)
    dp = [0] * (n + 1)
    stack = [1]
    w = float('inf')
    x = -1
    
    while stack:
        node = stack[-1]
        if node not in visited:
            count = 0
            for kid in edges[node]:
                if parents[kid] == -1:
                    if kid != 1:
                        parents[kid] = node
                elif kid != parents[node]:
                    if kid in visited:
                        count += 1
                    else:
                        stack.append(kid)
            if node == 1:
                count -= 1
            if count == len(edges[node]) - 1:
                stack.pop()
                visited.add(node)
                max_val = 0
                for kid in edges[node]:
                    dp[node] += dp[kid]
                    max_val = max(max_val, dp[kid])
                dp[node] += 1
                max_val = max(max_val, n - dp[node])
                if max_val < w:
                    w = max_val
                    x = node
                elif max_val == w:
                    x = min(x, node)
    
    return (x, w)