"""
QUESTION:
The "BerCorp" company has got n employees. These employees can use m approved official languages for the formal correspondence. The languages are numbered with integers from 1 to m. For each employee we have the list of languages, which he knows. This list could be empty, i. e. an employee may know no official languages. But the employees are willing to learn any number of official languages, as long as the company pays their lessons. A study course in one language for one employee costs 1 berdollar.

Find the minimum sum of money the company needs to spend so as any employee could correspond to any other one (their correspondence can be indirect, i. e. other employees can help out translating).

Input

The first line contains two integers n and m (2 ≤ n, m ≤ 100) — the number of employees and the number of languages.

Then n lines follow — each employee's language list. At the beginning of the i-th line is integer ki (0 ≤ ki ≤ m) — the number of languages the i-th employee knows. Next, the i-th line contains ki integers — aij (1 ≤ aij ≤ m) — the identifiers of languages the i-th employee knows. It is guaranteed that all the identifiers in one list are distinct. Note that an employee may know zero languages.

The numbers in the lines are separated by single spaces.

Output

Print a single integer — the minimum amount of money to pay so that in the end every employee could write a letter to every other one (other employees can help out translating).

Examples

Input

5 5
1 2
2 2 3
2 3 4
2 4 5
1 5


Output

0


Input

8 7
0
3 1 2 3
1 1
2 5 4
2 6 7
1 3
2 7 4
1 1


Output

2


Input

2 2
1 2
0


Output

1

Note

In the second sample the employee 1 can learn language 2, and employee 8 can learn language 4.

In the third sample employee 2 must learn language 2.
"""

class UnionFind:
    def __init__(self, n, m):
        self.data = [i for i in range(n + m)]
        self.size = [0] * (m + n)

    def union(self, u, v):
        up = self.find(u)
        vp = self.find(v)
        if up == vp:
            return
        if self.size[up] <= self.size[vp]:
            self.data[up] = vp
            self.size[vp] += self.size[up]
        else:
            self.data[vp] = up
            self.size[up] += self.size[vp]

    def find(self, v):
        if v != self.data[v]:
            self.data[v] = self.find(self.data[v])
        return self.data[v]

def minimum_berdollar_cost(n, m, employee_languages):
    uf = UnionFind(n, m)
    any_language_learned = False
    
    for i in range(n):
        k = len(employee_languages[i])
        for language in employee_languages[i]:
            language_index = language - 1 + n
            uf.union(i, language_index)
            any_language_learned = True
    
    languages = set()
    for i in range(n):
        language = uf.find(i)
        languages.add(language)
    
    if any_language_learned:
        return len(languages) - 1
    else:
        return n