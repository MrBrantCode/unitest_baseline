"""
QUESTION:
There are many anime that are about "love triangles": Alice loves Bob, and Charlie loves Bob as well, but Alice hates Charlie. You are thinking about an anime which has n characters. The characters are labeled from 1 to n. Every pair of two characters can either mutually love each other or mutually hate each other (there is no neutral state).

You hate love triangles (A-B are in love and B-C are in love, but A-C hate each other), and you also hate it when nobody is in love. So, considering any three characters, you will be happy if exactly one pair is in love (A and B love each other, and C hates both A and B), or if all three pairs are in love (A loves B, B loves C, C loves A).

You are given a list of m known relationships in the anime. You know for sure that certain pairs love each other, and certain pairs hate each other. You're wondering how many ways you can fill in the remaining relationships so you are happy with every triangle. Two ways are considered different if two characters are in love in one way but hate each other in the other. Print this count modulo 1 000 000 007.


-----Input-----

The first line of input will contain two integers n, m (3 ≤ n ≤ 100 000, 0 ≤ m ≤ 100 000).

The next m lines will contain the description of the known relationships. The i-th line will contain three integers a_{i}, b_{i}, c_{i}. If c_{i} is 1, then a_{i} and b_{i} are in love, otherwise, they hate each other (1 ≤ a_{i}, b_{i} ≤ n, a_{i} ≠ b_{i}, $c_{i} \in \{0,1 \}$).

Each pair of people will be described no more than once.


-----Output-----

Print a single integer equal to the number of ways to fill in the remaining pairs so that you are happy with every triangle modulo 1 000 000 007. 


-----Examples-----
Input
3 0

Output
4

Input
4 4
1 2 1
2 3 1
3 4 0
4 1 0

Output
1

Input
4 4
1 2 1
2 3 1
3 4 0
4 1 1

Output
0



-----Note-----

In the first sample, the four ways are to:   Make everyone love each other  Make 1 and 2 love each other, and 3 hate 1 and 2 (symmetrically, we get 3 ways from this). 

In the second sample, the only possible solution is to make 1 and 3 love each other and 2 and 4 hate each other.
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num = n

    def union(self, x, y):
        self._link(self.find_set(x), self.find_set(y))

    def _link(self, x, y):
        if x == y:
            return
        self.num -= 1
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        xp = self.parent[x]
        if xp != x:
            self.parent[x] = self.find_set(xp)
        return self.parent[x]

def count_happy_relationships(n, m, relationships):
    ds = DisjointSet(n * 2)
    
    for (a, b, c) in relationships:
        a -= 1
        b -= 1
        aA = a * 2
        aB = aA + 1
        bA = b * 2
        bB = bA + 1
        
        if c == 0:
            if ds.find_set(aA) == ds.find_set(bA):
                return 0
            ds.union(aA, bB)
            ds.union(aB, bA)
        else:
            if ds.find_set(aA) == ds.find_set(bB):
                return 0
            ds.union(aA, bA)
            ds.union(aB, bB)
    
    return pow(2, ds.num // 2 - 1, 10 ** 9 + 7)