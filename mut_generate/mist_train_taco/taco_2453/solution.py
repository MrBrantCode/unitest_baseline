"""
QUESTION:
Shuseki Kingdom is the world's leading nation for innovation and technology. There are n cities in the kingdom, numbered from 1 to n.

Thanks to Mr. Kitayuta's research, it has finally become possible to construct teleportation pipes between two cities. A teleportation pipe will connect two cities unidirectionally, that is, a teleportation pipe from city x to city y cannot be used to travel from city y to city x. The transportation within each city is extremely developed, therefore if a pipe from city x to city y and a pipe from city y to city z are both constructed, people will be able to travel from city x to city z instantly.

Mr. Kitayuta is also involved in national politics. He considers that the transportation between the m pairs of city (a_{i}, b_{i}) (1 ≤ i ≤ m) is important. He is planning to construct teleportation pipes so that for each important pair (a_{i}, b_{i}), it will be possible to travel from city a_{i} to city b_{i} by using one or more teleportation pipes (but not necessarily from city b_{i} to city a_{i}). Find the minimum number of teleportation pipes that need to be constructed. So far, no teleportation pipe has been constructed, and there is no other effective transportation between cities.


-----Input-----

The first line contains two space-separated integers n and m (2 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^5), denoting the number of the cities in Shuseki Kingdom and the number of the important pairs, respectively.

The following m lines describe the important pairs. The i-th of them (1 ≤ i ≤ m) contains two space-separated integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ n, a_{i} ≠ b_{i}), denoting that it must be possible to travel from city a_{i} to city b_{i} by using one or more teleportation pipes (but not necessarily from city b_{i} to city a_{i}). It is guaranteed that all pairs (a_{i}, b_{i}) are distinct.


-----Output-----

Print the minimum required number of teleportation pipes to fulfill Mr. Kitayuta's purpose.


-----Examples-----
Input
4 5
1 2
1 3
1 4
2 3
2 4

Output
3

Input
4 6
1 2
1 4
2 3
2 4
3 2
3 4

Output
4



-----Note-----

For the first sample, one of the optimal ways to construct pipes is shown in the image below:  [Image] 

For the second sample, one of the optimal ways is shown below:  [Image]
"""

def minimum_teleportation_pipes(n, m, pairs):
    n += 1
    cluster = list(range(n))
    dest = [0] * n
    ab = [[] for _ in range(n)]

    def root(x):
        if x != cluster[x]:
            cluster[x] = x = root(cluster[x])
        return x

    for a, b in pairs:
        ab[a].append(b)
        dest[b] += 1
        cluster[root(a)] = root(b)

    pool = [a for a, f in enumerate(dest) if not f]
    for a in pool:
        for b in ab[a]:
            dest[b] -= 1
            if not dest[b]:
                pool.append(b)

    ab = [True] * n
    for a, f in enumerate(dest):
        if f:
            ab[root(a)] = False

    return n - sum((f and a == c for a, c, f in zip(range(n), cluster, ab)))