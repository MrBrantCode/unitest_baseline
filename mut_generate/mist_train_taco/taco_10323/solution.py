"""
QUESTION:
There are N cards placed face down in a row. On each card, an integer 1 or 2 is written.
Let A_i be the integer written on the i-th card.
Your objective is to guess A_1, A_2, ..., A_N correctly.
You know the following facts:
 - For each i = 1, 2, ..., M, the value A_{X_i} + A_{Y_i} + Z_i is an even number.
You are a magician and can use the following magic any number of times:
Magic: Choose one card and know the integer A_i written on it. The cost of using this magic is 1.
What is the minimum cost required to determine all of A_1, A_2, ..., A_N?
It is guaranteed that there is no contradiction in given input.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 10^5
 - 1 \leq M \leq 10^5
 - 1 \leq X_i < Y_i \leq N
 - 1 \leq Z_i \leq 100
 - The pairs (X_i, Y_i) are distinct.
 - There is no contradiction in input. (That is, there exist integers A_1, A_2, ..., A_N that satisfy the conditions.)

-----Input-----
Input is given from Standard Input in the following format:
N M
X_1 Y_1 Z_1
X_2 Y_2 Z_2
\vdots
X_M Y_M Z_M

-----Output-----
Print the minimum total cost required to determine all of A_1, A_2, ..., A_N.

-----Sample Input-----
3 1
1 2 1

-----Sample Output-----
2

You can determine all of A_1, A_2, A_3 by using the magic for the first and third cards.
"""

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))

def minimum_cost_to_determine_cards(N, M, conditions):
    uf = UnionFind(N)
    for (X, Y, Z) in conditions:
        uf.union(X - 1, Y - 1)
    return len(uf.roots())