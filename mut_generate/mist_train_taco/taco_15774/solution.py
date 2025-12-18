"""
QUESTION:
You received a card with an integer $S$ and a multiplication table of infinite size. All the elements in the table are integers, and an integer at the $i$-th row from the top and the $j$-th column from the left is $A_{i,j} = i \times j$ ($i,j \geq 1$). The table has infinite size, i.e., the number of the rows and the number of the columns are infinite.

You love rectangular regions of the table in which the sum of numbers is $S$. Your task is to count the number of integer tuples $(a, b, c, d)$ that satisfies $1 \leq a \leq b, 1 \leq c \leq d$ and $\sum_{i=a}^b \sum_{j=c}^d A_{i,j} = S$.



Input

The input consists of a single test case of the following form.


$S$


The first line consists of one integer $S$ ($1 \leq S \leq 10^5$), representing the summation of rectangular regions you have to find.

Output

Print the number of rectangular regions whose summation is $S$ in one line.

Examples

Input

25


Output

10


Input

1


Output

1


Input

5


Output

4


Input

83160


Output

5120
"""

from collections import defaultdict
import sys

def count_rectangular_regions(S):
    def sum_range(a, b):
        return (b + a) * (b - a + 1) // 2

    def factorize(n):
        if n < 4:
            return [1, n]
        res = [1]
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                res.append(i)
                m = n // i
                if i != m:
                    res.append(m)
            i += 1
        res.append(n)
        return res

    if S == 1:
        return 1

    factors = factorize(S)
    f = defaultdict(lambda: 0)
    p = defaultdict(lambda: 1)
    factors.sort()

    for k in factors:
        for a in range(1, k + 1):
            b = k - a
            if a <= b:
                if p[a, b]:
                    f[sum_range(a, b)] += 1
                    p[a, b] = 0
        for a in range(1, S + 1):
            b = k + a - 1
            if p[a, b]:
                s_ = sum_range(a, b)
                if s_ > S:
                    break
                f[s_] += 1
                p[a, b] = 0

    ans = 0
    for k in factors:
        ans += f[k] * f[S // k]

    return ans