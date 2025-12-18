"""
QUESTION:
Quite recently a creative student Lesha had a lecture on trees. After the lecture Lesha was inspired and came up with the tree of his own which he called a k-tree.

A k-tree is an infinite rooted tree where:

  each vertex has exactly k children;  each edge has some weight;  if we look at the edges that goes from some vertex to its children (exactly k edges), then their weights will equal 1, 2, 3, ..., k. 

The picture below shows a part of a 3-tree.

 

 [Image]

    As soon as Dima, a good friend of Lesha, found out about the tree, he immediately wondered: "How many paths of total weight n (the sum of all weights of the edges in the path) are there, starting from the root of a k-tree and also containing at least one edge of weight at least d?".

Help Dima find an answer to his question. As the number of ways can be rather large, print it modulo 1000000007 (10^9 + 7). 


-----Input-----

A single line contains three space-separated integers: n, k and d (1 ≤ n, k ≤ 100; 1 ≤ d ≤ k).


-----Output-----

Print a single integer — the answer to the problem modulo 1000000007 (10^9 + 7). 


-----Examples-----
Input
3 3 2

Output
3

Input
3 3 3

Output
1

Input
4 3 2

Output
6

Input
4 5 2

Output
7
"""

def count_paths_with_weight(n: int, k: int, d: int) -> int:
    mod = 10 ** 9 + 7
    
    if d > n:
        return 0
    
    c = [0] * (n + 1)
    cod = [0] * (n + 1)
    
    for i in range(1, n + 1):
        c[i] = 1 if i <= k else 0
        cod[i] = 1 if i < d else 0
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                break
            else:
                c[i] = (c[i] + c[i - j]) % mod
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                break
            elif j < d:
                cod[i] = (cod[i] + cod[i - j]) % mod
    
    return (c[n] - cod[n]) % mod