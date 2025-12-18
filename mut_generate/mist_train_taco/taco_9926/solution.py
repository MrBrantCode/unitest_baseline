"""
QUESTION:
Long ago, you thought of two finite arithmetic progressions $A$ and $B$. Then you found out another sequence $C$ containing all elements common to both $A$ and $B$. It is not hard to see that $C$ is also a finite arithmetic progression. After many years, you forgot what $A$ was but remember $B$ and $C$. You are, for some reason, determined to find this lost arithmetic progression. Before you begin this eternal search, you want to know how many different finite arithmetic progressions exist which can be your lost progression $A$.

Two arithmetic progressions are considered different if they differ in their first term, common difference or number of terms.

It may be possible that there are infinitely many such progressions, in which case you won't even try to look for them! Print $-1$ in all such cases.

Even if there are finite number of them, the answer might be very large. So, you are only interested to find the answer modulo $10^9+7$.


-----Input-----

The first line of input contains a single integer $t$ ($1\leq t\leq 100$) denoting the number of testcases.

The first line of each testcase contains three integers $b$, $q$ and $y$ ($-10^9\leq b\leq 10^9$, $1\leq q\leq 10^9$, $2\leq y\leq 10^9$) denoting the first term, common difference and number of terms of $B$ respectively.

The second line of each testcase contains three integers $c$, $r$ and $z$ ($-10^9\leq c\leq 10^9$, $1\leq r\leq 10^9$, $2\leq z\leq 10^9$) denoting the first term, common difference and number of terms of $C$ respectively.


-----Output-----

For each testcase, print a single line containing a single integer.

If there are infinitely many finite arithmetic progressions which could be your lost progression $A$, print $-1$.

Otherwise, print the number of finite arithmetic progressions which could be your lost progression $A$ modulo $10^9+7$. In particular, if there are no such finite arithmetic progressions, print $0$.


-----Examples-----

Input
8
-3 1 7
-1 2 4
-9 3 11
0 6 3
2 5 5
7 5 4
2 2 11
10 5 3
0 2 9
2 4 3
-11 4 12
1 12 2
-27 4 7
-17 8 2
-8400 420 1000000000
0 4620 10
Output
0
10
-1
0
-1
21
0
273000


-----Note-----

For the first testcase, $B={-3,-2,-1,0,1,2,3\}$ and $C={-1,1,3,5\}$. There is no such arithmetic progression which can be equal to $A$ because $5$ is not present in $B$ and for any $A$, $5$ should not be present in $C$ also.

For the second testcase, $B={-9,-6,-3,0,3,6,9,12,15,18,21\}$ and $C={0,6,12\}$. There are $10$ possible arithmetic progressions which can be $A$:

$\{0,6,12\}$

$\{0,2,4,6,8,10,12\}$

$\{0,2,4,6,8,10,12,14\}$

$\{0,2,4,6,8,10,12,14,16\}$

$\{-2,0,2,4,6,8,10,12\}$

$\{-2,0,2,4,6,8,10,12,14\}$

$\{-2,0,2,4,6,8,10,12,14,16\}$

$\{-4,-2,0,2,4,6,8,10,12\}$

$\{-4,-2,0,2,4,6,8,10,12,14\}$

$\{-4,-2,0,2,4,6,8,10,12,14,16\}$

For the third testcase, $B={2,7,12,17,22\}$ and $C={7,12,17,22\}$. There are infinitely many arithmetic progressions which can be $A$ like:

$\{7,12,17,22\}$

$\{7,12,17,22,27\}$

$\{7,12,17,22,27,32\}$

$\{7,12,17,22,27,32,37\}$

$\{7,12,17,22,27,32,37,42\}$

$\ldots$
"""

large_int = 10 ** 9 + 7

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def factors(n):
    return set((factor for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for factor in (i, n // i)))

def count_possible_progressions(b_start, b_step, b_n, c_start, c_step, c_n):
    if c_step % b_step != 0 or (c_start - b_start) % b_step != 0 or c_start < b_start or (c_start + (c_n - 1) * c_step > b_start + (b_n - 1) * b_step):
        return 0
    if c_start + c_n * c_step > b_start + (b_n - 1) * b_step or c_start - c_step < b_start:
        return -1
    count = 0
    for i in factors(c_step):
        if i < c_step // b_step or lcm(b_step, i) < c_step:
            continue
        count += c_step // i * (c_step // i)
    return count % large_int