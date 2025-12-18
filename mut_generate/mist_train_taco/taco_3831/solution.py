"""
QUESTION:
problem

There are $ N $ propositions, named $ 1, 2, \ cdots, N $, respectively. Also, $ M $ information about the propositions is given. The $ i $ th information is "$ a_i $$". Given in the form "b_i $", which means that $ a_i $ is $ b_i $. ("If" is a logical conditional and the transition law holds.) $ For each proposition $ i $ Output all propositions that have the same value as i $ in ascending order. However, proposition $ i $ and proposition $ i $ are always the same value. Proposition $ X $ and proposition $ Y $ have the same value as "$ if $ X $". It means "Y $" and "$ X $ if $ Y $".



output

On the $ i $ line, output all propositions that have the same value as the proposition $ i $, separated by blanks in ascending order. Also, output a line break at the end of each line.

Example

Input

5 2
1 2
2 1


Output

1 2
1 2
3
4
5
"""

def find_same_value_propositions(N, M, info):
    G = [[] for _ in range(N)]
    rG = [[] for _ in range(N)]
    
    for (a, b) in info:
        G[a - 1].append(b - 1)
        rG[b - 1].append(a - 1)

    def SCC(G, rG):
        N = len(G)

        def dfs(i):
            nonlocal t, rorder, searched
            searched[i] = True
            for j in G[i]:
                if not searched[j]:
                    dfs(j)
            rorder[t] = i
            t += 1

        def rdfs(i):
            nonlocal t, group, g
            group[i] = g
            for j in rG[i]:
                if group[j] == -1:
                    rdfs(j)
        
        t = 0
        rorder = [-1] * N
        searched = [False] * N
        group = [-1] * N
        for i in range(N):
            if not searched[i]:
                dfs(i)
        
        g = 0
        for i in range(N - 1, -1, -1):
            if group[rorder[i]] == -1:
                rdfs(rorder[i])
                g += 1
        return (group, g)
    
    (group, g) = SCC(G, rG)
    ans = [[] for _ in range(g)]
    
    for i in range(N):
        ans[group[i]].append(i + 1)
    
    result = []
    for i in range(N):
        result.append(sorted(ans[group[i]]))
    
    return result