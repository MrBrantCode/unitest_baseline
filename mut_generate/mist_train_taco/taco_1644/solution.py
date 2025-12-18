"""
QUESTION:
You are given a grid with dimension $n$ x $m$ and two points with coordinates $X(x1,y1)$ and $Y(x2,y2)$ . Your task is to find the number of ways in which one can go from point $A(0, 0)$ to point $B (n, m)$ using the $shortest$ possible path such that the shortest path neither passes through $X$ nor through $Y$. 

Consider the above 4 x 4 grid . Our shortest path can't pass through points (1,3) and (3,3) (marked by yellow dots). One of the possible shortest path is from $A$ to $C$ and then from $C$ to $B$.

-----Input:-----
- First line contains $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, six space separated integers $n, m, x1, y1, x2, y2$. 

-----Output:-----
- For each testcase, output in a single line number of ways modulo $998244353$.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $3 \leq n,m \leq 10^5$
- $1 \leq x1, x2 \leq n - 1$
- $1 \leq y1, y2 \leq m - 1$
- $x1 \leq x2$
- $y1 \leq y2$
- $X$ and $Y$ never coincide.

-----Sample Input:-----
1
3 3 1 1 1 2

-----Sample Output:-----
5
"""

def count_shortest_paths_avoiding_points(n, m, x1, y1, x2, y2):
    N = 100001
    p = 998244353
    factorialNumInverse = [0] * (N + 1)
    naturalNumInverse = [0] * (N + 1)
    fact = [0] * (N + 1)

    def InverseofNumber(p):
        naturalNumInverse[0] = naturalNumInverse[1] = 1
        for i in range(2, N + 1):
            naturalNumInverse[i] = naturalNumInverse[p % i] * (p - p // i) % p

    def InverseofFactorial(p):
        factorialNumInverse[0] = factorialNumInverse[1] = 1
        for i in range(2, N + 1):
            factorialNumInverse[i] = naturalNumInverse[i] * factorialNumInverse[i - 1] % p

    def factorial(p):
        fact[0] = 1
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % p

    def f(num, den1, den2):
        ans = fact[num] * factorialNumInverse[den1] % p * factorialNumInverse[den2] % p
        return ans

    InverseofNumber(p)
    InverseofFactorial(p)
    factorial(p)

    tot = f(m + n, m, n)
    a = f(m - y1 + n - x1, m - y1, n - x1)
    aa = f(x1 + y1, x1, y1)
    b = f(m - y2 + n - x2, m - y2, n - x2)
    bb = f(x2 + y2, x2, y2)
    c = f(y2 - y1 + x2 - x1, y2 - y1, x2 - x1)
    ans = (tot - a * aa - b * bb + c * aa * b) % p

    return ans