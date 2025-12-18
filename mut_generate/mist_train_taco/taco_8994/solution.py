"""
QUESTION:
Mr. Dango's family has an extremely huge number of members. Once it had about 100 members, and now it has as many as population of a city. It is jokingly guessed that the member might fill this planet in the near future.

Mr. Dango's family, the huge family, is getting their new house. Scale of the house is as large as that of town.

They all had warm and gracious personality and were close each other. However, in this year the two members of them became to hate each other. Since the two members had enormous influence in the family, they were split into two groups.

They hope that the two groups don't meet each other in the new house. Though they are in the same building, they can avoid to meet each other by adjusting passageways.

Now, you have a figure of room layout. Your task is written below.

You have to decide the two groups each room should belong to. Besides you must make it impossible that they move from any rooms belonging to one group to any rooms belonging to the other group. All of the rooms need to belong to exactly one group. And any group has at least one room.

To do the task, you can cancel building passageway. Because the house is under construction, to cancel causes some cost. You'll be given the number of rooms and information of passageway. You have to do the task by the lowest cost.

Please answer the lowest cost.

By characteristics of Mr. Dango's family, they move very slowly. So all passageways are escalators. Because of it, the passageways are one-way.

Constraints

* 2 ≤ n  ≤ 100
* -10,000 ≤ Ci ≤ 10,000
* Y1 ... Ym can't be duplicated integer by each other.

Input

The input consists of multiple datasets. Each dataset is given in the following format.


n m
X1 Y1 C1
...
Xm Ym Cm


All numbers in each datasets are integers. The integers in each line are separated by a space.

The first line of each datasets contains two integers. n is the number of rooms in the house, m is the number of passageways in the house. Each room is indexed from 0 to n-1.

Each of following  m  lines gives the details of the passageways in the house. Each line contains three integers. The first integer Xi is an index of the room, the starting point of the passageway. The second integer Yi is an index of the room, the end point of the passageway. The third integer Ci is the cost to cancel construction of the passageway. The passageways, they are escalators, are one-way. The last dataset is followed by a line containing two zeros (separated by a space).

Output

For each dataset, print the lowest cost in a line. You may assume that the all of integers of both the answers and the input can be represented by 32 bits signed integers.

Example

Input

3 2
0 1 2
1 2 1
2 1
0 1 100
2 1
0 1 0
2 1
0 1 -1
0 0


Output

1
100
0
-1
"""

class UnionSet:
    def __init__(self, nmax):
        self.size = [1] * nmax
        self.id = [i for i in range(nmax + 1)]

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def unite(self, p, q):
        (i, j) = (self.root(p), self.root(q))
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

def calculate_lowest_cost(n, m, passageways):
    u = UnionSet(n)
    ans = 0
    tbl = []
    
    for (x, y, c) in passageways:
        if c < 0:
            ans += c
        else:
            tbl.append((c, x, y))
    
    tbl.sort(reverse=True)
    
    for (c, x, y) in tbl:
        if not u.connected(x, y):
            if n > 2:
                n -= 1
                u.unite(x, y)
            else:
                ans += c
    
    return ans