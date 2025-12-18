"""
QUESTION:
Read problem statements in [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a sequence $A_{1}, A_{2}, \ldots, A_{N}$. Chef wants you to handle $Q$ queries. There are two types of queries:
1 L R X: for each $i$ ($L ≤ i ≤ R$), add $(X + i - L)^2$ to $A_{i}$
2 Y: find the current value of $A_{Y}$

------  Input ------
The first line of the input contains two space-separated integers $N$ and $Q$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.
$Q$ lines follow. Each of these lines describes a query in the format described above.

------  Output ------
For each query of the second type, print a single line containing one integer $A_{Y}$.

------  Constraints ------
$1 ≤ N, Q ≤ 10^{5}$
$0 ≤ |A_{i}| ≤ 10^{6}$ for each valid $i$
$1 ≤ L ≤ R ≤ N$
$0 ≤ |X| ≤ 10^{6}$
$1 ≤ Y ≤ N$

----- Sample Input 1 ------ 
5 4
1 10 3 6 5
1 1 3 5
2 3
1 4 5 7
2 5
----- Sample Output 1 ------ 
52
69
----- explanation 1 ------ 
- the sequence after the first query is $[1 + 5^{2}, 10 + (5 + 2 - 1)^2, 3 + (5 + 3 - 1)^2, 6, 5] = [26,  46, 52, 6, 5]$
- the second query asks for $A_{3}$, which is $52$
- the sequence after the third query is $[26,  46, 52, 6 + 7^{2}, 5 + (7+1)^2] = [26,  46, 52, 55, 69]$
- the fourth query asks for $A_{5}$, which is $69$
"""

def process_queries(N, Q, A, queries):
    class Ftree:
        def __init__(self, N):
            self.st = [0] * (N + 1)
            self.n = N

        def Update(self, l, r, diff):
            while l <= self.n:
                self.st[l] += diff
                l += l & -l
            r += 1
            while r <= self.n:
                self.st[r] -= diff
                r += r & -r

        def Query(self, i):
            sum = 0
            while i > 0:
                sum += self.st[i]
                i -= i & -i
            return sum

    A.insert(0, 0)
    b1 = Ftree(N)
    b2 = Ftree(N)
    b3 = Ftree(N)
    results = []

    for q in queries:
        if q[0] == 1:
            L = q[1]
            R = q[2]
            X = q[3]
            y = X - L
            b1.Update(L, R, y ** 2)
            b2.Update(L, R, 2 * y)
            b3.Update(L, R, 1)
        elif q[0] == 2:
            i = q[1]
            result = A[i] + b1.Query(i) + b2.Query(i) * i + b3.Query(i) * i * i
            results.append(result)

    return results