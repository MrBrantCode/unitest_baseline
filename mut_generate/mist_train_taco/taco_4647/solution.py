"""
QUESTION:
Consider a sequence, $c_0,c_1,\ldots c_{n-1}$, and a polynomial of degree $1$ defined as $Q(x)=a\cdot x+b$. You must perform $\textit{q}$ queries on the sequence, where each query is one of the following two types:

1 i x: Replace $c_i$ with $\boldsymbol{x}$.
2 l r: Consider the polynomial $P(x)=c_l\cdot x^0+c_{l+1}\cdot x^1+\cdots+c_r\cdot x^{r-l}$ and determine whether $P(x)$ is divisible by $Q(x)=a\cdot x+b$ over the field $Z_p$, where $p=10^9+7$. In other words, check if there exists a polynomial $R(x)$ with integer coefficients such that each coefficient of $P(x)-R(x)\cdot Q(x)$ is divisible by $\boldsymbol{p}$. If a valid $R(x)$ exists, print Yes on a new line; otherwise, print No.

Given the values of $n$, $\class{ML__boldsymbol}{\boldsymbol{a}}$, $\boldsymbol{b}$, and $\textit{q}$ queries, perform each query in order.

Input Format

The first line contains four space-separated integers describing the respective values of $n$ (the length of the sequence), $\class{ML__boldsymbol}{\boldsymbol{a}}$ (a coefficient in $Q(x)$), $\boldsymbol{b}$ (a coefficient in $Q(x)$), and $\textit{q}$ (the number of queries). 

The second line contains $n$ space-separated integers describing $c_0,c_1,\ldots c_{n-1}$. 

Each of the $\textit{q}$ subsequent lines contains three space-separated integers describing a query of either type 1 or type 2.

Constraints

$1\leq n,q\leq10^5$
For query type 1: $0\leq i\leq n-1$ and $0\leq x<10^9+7$.
For query type 2: $0\leq l\leq r\leq n-1$.
$0\leq a,b,c_i<10^9+7$
$a\neq0$

Output Format

For each query of type 2, print Yes on a new line if $Q(x)$ is a divisor of $P(x)$; otherwise, print No instead.

Sample Input 0
3 2 2 3
1 2 3
2 0 2
1 2 1
2 0 2

Sample Output 0
No
Yes

Explanation 0

Given $Q(x)=2\cdot x+2$ and the initial sequence $c=\{1,2,3\}$, we perform the following $q=3$ queries:

$Q(x)=2\cdot x+2$ is not a divisor of $P(x)=1+2\cdot x+3\cdot x^2$, so we print No on a new line.
Set $c_2$ to $1$, so $c=\{1,2,1\}$.
After the second query, $P(x)=1+2\cdot x+1\cdot x^2$. Because $(2\cdot x+2)\cdot(500000004\cdot x+500000004)\text{mod}(10^9+7)=1+2\cdot x+1\cdot x^2=P(x)$, we print Yes on a new line.
"""

def process_queries(n, a, b, q, c, queries):
    def init(R, x, p):
        T = [R]
        while len(R) > 1:
            if len(R) & 1:
                R.append(0)
            R = [(R[i] + x * R[i + 1]) % p for i in range(0, len(R), 2)]
            x = x * x % p
            T.append(R)
        return T

    def update(T, i, x, p):
        S = T[0]
        for j in range(1, len(T)):
            R = T[j]
            i >>= 1
            R[i] = (S[2 * i] + x * S[2 * i + 1]) % p
            S = R
            x = x * x % p

    def query(T, i, x, p):
        if i == 0:
            return T[-1][0]
        s = 0
        y = 1
        for j in range(len(T) - 1):
            if i & 1:
                s = (s + y * T[j][i]) % p
                y = y * x % p
            i = i + 1 >> 1
            x = x * x % p
        return s

    p = 10 ** 9 + 7
    x = -b * pow(a, p - 2, p) % p
    T = init(c, x, p)
    results = []

    for k, a, b in queries:
        if k == 1:
            c[a] = b
            update(T, a, x, p)
        elif k == 2:
            y = (query(T, a, x, p) - query(T, b + 1, x, p) * pow(x, b - a + 1, p)) % p
            results.append('Yes' if y == 0 else 'No')

    return results