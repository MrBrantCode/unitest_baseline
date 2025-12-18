"""
QUESTION:
Aoki is playing with a sequence of numbers a_{1}, a_{2}, ..., a_{N}. Every second, he performs the following operation :

* Choose a positive integer k. For each element of the sequence v, Aoki may choose to replace v with its remainder when divided by k, or do nothing with v. The cost of this operation is 2^{k} (regardless of how many elements he changes).



Aoki wants to turn the sequence into b_{1}, b_{2}, ..., b_{N} (the order of the elements is important). Determine if it is possible for Aoki to perform this task and if yes, find the minimum cost required.

Constraints

* 1 \leq N \leq 50
* 0 \leq a_{i}, b_{i} \leq 50
* All values in the input are integers.

Input

Input is given from Standard Input in the following format:


N
a_{1} a_{2} ... a_{N}
b_{1} b_{2} ... b_{N}


Output

Print the minimum cost required to turn the original sequence into b_{1}, b_{2}, ..., b_{N}. If the task is impossible, output -1 instead.

Examples

Input

3
19 10 14
0 3 4


Output

160


Input

3
19 15 14
0 0 0


Output

2


Input

2
8 13
5 13


Output

-1


Input

4
2 0 1 8
2 0 1 8


Output

0


Input

1
50
13


Output

137438953472
"""

def minimum_cost_to_transform_sequence(N, A, B):
    def inpl(seq):
        return tuple(map(int, seq.split()))
    
    def dfs(a, b, G):
        visited = [False] * (M + 1)
        Q = [a]
        while Q:
            p = Q.pop()
            if visited[p]:
                continue
            else:
                visited[p] = True
                for q in G[p]:
                    if q == b:
                        return True
                    if not visited[q]:
                        Q.append(q)
        return False
    
    # Check if any element in A is less than the corresponding element in B
    for (a, b) in zip(A, B):
        if a < b:
            return -1
    
    M = max(max(A), max(B))
    S = [i for i in range(1, M + 1)]
    T = len(S)
    
    found = False
    for i in range(M, 0, -1):
        del S[S.index(i)]
        G = [set() for _ in range(M + 1)]
        for j in range(1, M + 1):
            for s in S:
                G[j].add(j % s)
        for (a, b) in zip(A, B):
            if a == b:
                continue
            if not dfs(a, b, G):
                S.append(i)
                break
        else:
            found = True
    
    ans = 0
    for s in S:
        ans += 2 ** s
    
    if found:
        return ans
    else:
        return -1