"""
QUESTION:
Read problems statements [Hindi] , [Vietnamese] , [Mandarin Chinese] , [Russian] and [Bengali] as well.

Chef is making $N$ atomic soups numbered $1$ through $N$. Each soup is either a *base* atomic soup or a composition of other atomic soups. For each valid $i$, if soup $i$ is not a base soup, one unit of this soup is made by mixing together one unit of soup $c_{i, 1}$, one unit of soup $c_{i, 2}$, and so on to one unit of soup $c_{i, P_{i}}$. Note that these $P_{i}$ soup units are not necessarily from distinct soups and that we obtain only $1$ unit of soup by mixing $P_{i}$ units.

Due to their structure, two units of the same base atomic soup always cancel out and vanish when mixed together. Therefore, we define the *base decomposition* of a soup as the set of all base atomic soups that need to be used an odd number of times when making the resulting soup (i.e. a base soup $b$ belongs to the base decomposition if we need to use an odd number of units of soup $b$ in total). The base decomposition of a sequence of atomic soups is the base decomposition of the soup created by mixing together one unit of each of these soups.

You should answer $Q$ queries. In each query, you are given a sequence of Chef's soups $s_{1}, s_{2}, \dots, s_{K}$; you must decide whether it is possible to choose two disjoint subsequences (one of which may be empty) of this sequence which have the same base decomposition. Two subsequences are disjoint if there is no index $i$ such that each subsequence contains soup $s_{i}$.

------  Input ------
The first line of the input contains a single integer $N$.
$N$ lines follow. For each $i$ ($1 ≤ i ≤ N$), the $i$-th of these lines contains an integer $P_{i}$; if $P_{i} \neq 0$, it is followed by a space and $P_{i}$ space-separated integers $c_{i, 1}, c_{i, 2}, \ldots, c_{i, P_{i}}$.
The next line contains a single integer $Q$.
The following $Q$ lines describe queries. Each of these lines contains an integer $K$ followed by a space and $K$ space-separated integers $s_{1}, s_{2}, \dots, s_{K}$.

------  Output ------
Print a single line containing a string with length $Q$. For each valid $i$, the $i$-th character of this string should be '1' if it is possible to choose required subsequences in the $i$-th query or '0' otherwise.

------  Constraints  ------
$1 ≤ N, Q ≤ 2 \cdot 10^{4}$
$1 ≤ K ≤ 30$
$1 ≤ c_{i, j} < i$ for each valid $i, j$
$1 ≤ s_{i} ≤ N$ for each valid $i$
$P_{1} + P_{2} + \ldots + P_{N} ≤ 5 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (13 points):
$1 ≤ N ≤ 100$
$1 ≤ K ≤ 6$

Subtask #2 (22 points): $1 ≤ N ≤ 500$

Subtask #3 (65 points): original constraints

----- Sample Input 1 ------ 
8

0

0

2 1 2

0

3 1 2 4

3 2 2 3

2 2 4

2 1 4

5

3 3 4 5

4 2 4 1 5

3 1 2 4

4 2 4 3 1

4 6 7 8 5
----- Sample Output 1 ------ 
11011
----- explanation 1 ------ 
Soups $1$, $2$ and $4$ are base atomic soups. The base decompositions of the other soups are:
- soup $3$: $\{1, 2\}$
- soup $5$: $\{1, 2, 4\}$
- soup $6$: $\{1, 2\}$ (two units of soup $2$ cancel out)
- soup $7$: $\{2, 4\}$
- soup $8$: $\{1, 4\}$

For the first query, we can choose subsequences $[3, 4]$ and $[5]$. The base decomposition of subsequence $\{3, 4\}$ is $\{1, 2, 4\}$, which is the same as the base decomposition of soup $5$.

For the last query, we can choose subsequences $[6, 8]$ and $[7]$. The base decomposition of each subsequence is $\{2, 4\}$, because two units of soup $1$ cancel out. You may notice that the chosen subsequences do not form a partition of all $K$ given soups, since soup $5$ was not used at all.
"""

def can_form_disjoint_subsequences(N, recipes, queries):
    vectors = [0] * N
    d = 0
    
    # Construct the vectors for each soup
    for i in range(N):
        recipe = recipes[i]
        if recipe[0] == 0:
            vectors[i] = 1 << d
            d += 1
        else:
            for j in recipe[1:]:
                vectors[i] ^= vectors[j - 1]
    
    results = []
    
    # Process each query
    for query in queries:
        K = query[0]
        s = query[1:]
        vecs = [vectors[i - 1] for i in s]
        linear_dependence = False
        
        for i in range(K):
            for j in range(i):
                if vecs[i] ^ vecs[j] < vecs[i]:
                    vecs[i] ^= vecs[j]
            if vecs[i] == 0:
                linear_dependence = True
                break
        
        results.append('1' if linear_dependence else '0')
    
    return ''.join(results)