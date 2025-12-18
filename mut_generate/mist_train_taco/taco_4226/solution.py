"""
QUESTION:
Professor GukiZ has hobby — constructing different arrays. His best student, Nenad, gave him the following task that he just can't manage to solve:

Construct an $n$-element array, $\mbox{A}$, where the sum of all elements is equal to $\boldsymbol{\mathrm{~S~}}$ and the sum of absolute differences between each pair of elements is equal to $\boldsymbol{\mbox{k}}$. All elements in $\mbox{A}$ must be non-negative integers.

$A_0+A_1+\ldots+A_{n-1}=s$

$\sum_{i=0}^{n-1}\sum_{j=i}^{n-1}|A_i-A_j|=k$

If there is more then one such array, you need to find the lexicographically smallest one. In the case no such array $\mbox{A}$ exists, print $-1$.

Note: An array, $\mbox{A}$, is considered to be lexicographically smaller than another array, $\mbox{B}$, if there is an index $\boldsymbol{i}$ such that  $A_i<B_i$ and, for any index $j<i$, $A_j=B_j$.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. 

Each of the $\textit{q}$ subsequent lines contains three space-separated integers describing the respective values of $n$ (the number of elements in array $\mbox{A}$), $\boldsymbol{\mathrm{~S~}}$ (the sum of elements in $\mbox{A}$), and $\boldsymbol{\mbox{k}}$ (the sum of absolute differences between each pair of elements).

Constraints

$1\leq q\leq100$
$1\leq n\leq50$
$0\leq s\leq200$
$0\leq k\leq2000$

Subtasks

For $\textbf{10%}$ of the maximum score:

$1\leq q\leq10$
$1\leq n\leq5$
$0\leq s\leq10$
$0\leq k\leq20$

For $50\%$ of the maximum score:

$1\leq q\leq10$
$1\leq n\leq50$
$0\leq s\leq100$
$0\leq k\leq500$

Output Format

For each query, print $n$ space-separated integers describing the respective elements of the lexicographically smallest array $\mbox{A}$ satisfying the conditions given above. If no such array exists, print $-1$ instead.

Sample Input
 1
 3 3 4

Sample Output
 0 1 2

Explanation

We have $q=1$ query in which $n=3$, $s=3$, and $k=4$. The lexicographically smallest array is $A=[0,1,2]$. 

The sum of array $\mbox{A}$'s elements is $0+1+2=3\equiv s$

The absolute differences between each pair of elements are: 

$|A_0-A_1|=1$ 

$|A_0-A_2|=2$ 

$|A_1-A_2|=1$    

The sum of these absolute differences is $1+1+2=4\equiv k$ 

As array $\mbox{A}$ is both lexicographically smallest and satisfies the given conditions, we print its contents on a new line as 0 1 2.
"""

def construct_array(n, s, k):
    def mn(ceil, beans):
        return beans // ceil * cumsum[ceil] + cumsum[beans % ceil]

    def mx(ceil, beans):
        return cumsum[1] * beans

    fmemo = set()

    def f(ceil, sm, beans):
        if not mn(ceil, beans) <= sm <= mx(ceil, beans):
            return False
        if beans == 0 and sm == 0:
            return True
        if (ceil, sm, beans) in fmemo:
            return False
        for k in range(1, min(beans, ceil) + 1):
            if f(k, sm - cumsum[k], beans - k):
                res.append(k)
                return True
        fmemo.add((ceil, sm, beans))
        return False

    if n == 1:
        if k == 0:
            return [s]
        else:
            return [-1]

    if s == 0:
        if k == 0:
            return [0 for _ in range(n)]
        else:
            return [-1]

    cumsum = [0, 2 * n - 2]
    for i in range(1, n):
        cumsum.append(cumsum[-1] + 2 * n - 2 - 2 * i)

    res = []
    if f(n, k + (n - 1) * s, s):
        r = [0 for _ in range(n)]
        for num in res:
            for i in range(num):
                r[-1 - i] += 1
        return r
    else:
        return [-1]