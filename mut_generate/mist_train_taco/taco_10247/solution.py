"""
QUESTION:
You are given a sequence of $n$ integers, $a_0,a_1,\ldots,a_{n-1}$. Find and print any integer $\boldsymbol{x}$ such that $\boldsymbol{x}$ is divisor of every $a_i$ except for exactly one element.

Input Format

The first line contains an integer, $n$, denoting the length of the sequence. 

The second line contains $n$ positive space-separated integers describing $a_0,a_1,\ldots,a_{n-1}$.

Constraints

$1\leq n\leq10^5$
$1\leq a_i\leq10^{18}$
It is guaranteed that a solution exists.

Output Format

Print any positive integer denoting $\boldsymbol{x}$ such that $\boldsymbol{x}$ is a divisor of exactly $n-1$ of the sequence's elements. $\boldsymbol{x}$ must be between $\mbox{1}$ and $2\cdot10^{18}$

Sample Input 0
4
3 6 18 12

Sample Output 0
6

Explanation 0

We are given the array $[3,6,18,12]$. There are two possible answers:

$x=6$ is a divisor of $\boldsymbol{6}$, $12$, and $\mbox{18}$ but not a divisor of $3$.
$x=2$ is a divisor of $\boldsymbol{6}$, $12$, and $\mbox{18}$ but not a divisor of $3$.

Thus, we can print either $\boldsymbol{6}$ or $2$ as our answer.
"""

def find_divisor_except_one(n, a):
    if n == 1:
        return a[0] + 1

    def divn(d):
        return sum((num % d == 0 for num in a))

    def gcd(a, b):
        if min(a, b) == 0:
            return max(a, b)
        return gcd(b, a % b)

    g = a[0]
    for i in range(n):
        g = gcd(g, a[i])

    for i in range(n):
        a[i] //= g

    res = g
    culprit = -1
    g = a[0]
    for i in range(n):
        g = gcd(g, a[i])
        if g == 1:
            culprit = i
            break

    g = a[0 if culprit == -1 else 1]
    for i in range(n):
        if i != culprit:
            g = gcd(g, a[i])

    return res * g