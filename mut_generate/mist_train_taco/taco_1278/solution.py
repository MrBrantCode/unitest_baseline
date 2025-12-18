"""
QUESTION:
ByteLand is a large country with a tree-like road system. It has $N$ cities and $(N-1)$ unidirected roads. The capital of ByteLand is a city, numbered $\mbox{1}$, and all the roads go away from the capital. So people use these roads to reach any city from the capital. But it is impossible to reach the capital from a city by roads. 

To solve this problem, there is a system of teleporters. Each city has a teleporter in it. Each teleporter has a value of strength. Let's say, the $\boldsymbol{i}$-th one has the value of strength equal to $A_i$. This means that by using the teleporter, you'll become $A_i$ cities close to the capital (the same as going $A_i$ roads in the capital direction). If the distance to the capital is less than $A_i$, you'll simply move to the capital instead.

The road system of ByteLand and the initial teleports' strengths will be given to you. You'll also be given $\mbox{M}$ queries about the teleport network in ByteLand. These queries will have one of the following forms:

$\mbox{1}$ $\mbox{X}$ $\mathbf{Y}$ : The strength of the teleport in the city with the number $\mbox{X}$ becomes equal to $\mathbf{Y}$;

$2$ $\mbox{X}$ : Please output the minimal number of teleports that needs to be used to get from the city with the number $\mbox{X}$ to the capital. We can use only teleports in this query, but not the roads!

Input Format

The first line of input will contain two space-separated integers $N$ and $\mbox{M}$.

The second line will contain $N$ space separated integers $A_1,A_2,\ldots,A_N$ - the initial strengths of the teleports.

The following $(N-1)$ lines will contain pairs of space separated positive integers $\mbox{X}$ and $\mathbf{Y}$ with the meaning that there is a road between the cities with the numbers $\mbox{X}$ and $\mathbf{Y}$.

Each of following $\mbox{M}$ lines will contain a query in one of the formats, described above.

Constraints  

1 <= N <= 100000 

1 <= M <= 100000 

1 <= A_{i} <= 10000

Output Format

For each query of the second type, output an answer on a separate line. 

Sample Input
5 2
1 2 1 2 1
1 2
2 3
3 4
4 5
2 4
2 5

Sample Output
2
3

Explanation

In the first query, we jump two cities up and appear in the second city, then we jump once more and move to the capital.

In the second query, we jump one city up and appear in the city $\begin{array}{c}4\end{array}$. From that city we need $2$ more teleportations to get to the capital (this is yet the first query).
"""

def calculate_teleport_steps(n, m, teleporters, roads, queries):
    # Initialize paths
    paths = [[] for _ in range(n)]
    
    # Build the paths based on the roads
    for a, b in roads:
        a -= 1
        b -= 1
        if not paths[a]:
            paths[b].append([a, b])
        for path in paths[a]:
            paths[b].append(path + [b])
    
    results = []
    
    # Process each query
    for query in queries:
        if query[0] == 1:
            # Update the strength of the teleport in city X to Y
            _, X, Y = query
            teleporters[X - 1] = Y
        elif query[0] == 2:
            # Calculate the minimal number of teleports to get from city X to the capital
            _, X = query
            x = X - 1
            tmp = -1
            for path in paths[x]:
                res = 0
                j = len(path)
                while j > 1:
                    j -= teleporters[j - 1]
                    res += 1
                if tmp < 0 or tmp > res:
                    tmp = res
            results.append(tmp)
    
    return results