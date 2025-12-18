"""
QUESTION:
Paprika loves permutations. She has an array $a_1, a_2, \dots, a_n$. She wants to make the array a permutation of integers $1$ to $n$.

In order to achieve this goal, she can perform operations on the array. In each operation she can choose two integers $i$ ($1 \le i \le n$) and $x$ ($x > 0$), then perform $a_i := a_i mod x$ (that is, replace $a_i$ by the remainder of $a_i$ divided by $x$). In different operations, the chosen $i$ and $x$ can be different.

Determine the minimum number of operations needed to make the array a permutation of integers $1$ to $n$. If it is impossible, output $-1$.

A permutation is an array consisting of $n$ distinct integers from $1$ to $n$ in arbitrary order. For example, $[2,3,1,5,4]$ is a permutation, but $[1,2,2]$ is not a permutation ($2$ appears twice in the array) and $[1,3,4]$ is also not a permutation ($n=3$ but there is $4$ in the array).


-----Input-----

Each test contains multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Description of the test cases follows.

The first line of each test case contains an integer $n$ ($1 \le n \le 10^5$).

The second line of each test case contains $n$ integers $a_1, a_2, \dots, a_n$. ($1 \le a_i \le 10^9$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output the minimum number of operations needed to make the array a permutation of integers $1$ to $n$, or $-1$ if it is impossible.


-----Examples-----

Input
4
2
1 7
3
1 5 4
4
12345678 87654321 20211218 23571113
9
1 2 3 4 18 19 5 6 7
Output
1
-1
4
2


-----Note-----

For the first test, the only possible sequence of operations which minimizes the number of operations is:

Choose $i=2$, $x=5$. Perform $a_2 := a_2 mod 5 = 2$.

For the second test, it is impossible to obtain a permutation of integers from $1$ to $n$.
"""

def min_operations_to_permutation(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        a = a + [0]
        b = [-1] * (n + 1)
        a.sort()
        
        for i in a:
            if i <= n:
                b[i] += 1
        
        c = 0
        j = 1
        i = 1
        
        while j <= n:
            if b[j] < 0:
                if a[i] > n or b[a[i]]:
                    if a[i] <= n:
                        b[a[i]] -= 1
                    if a[i] > 2 * j:
                        c += 1
                        j += 1
                        i += 1
                    else:
                        results.append(-1)
                        break
                elif b[a[i]] == 0:
                    i += 1
            else:
                j += 1
        else:
            results.append(c)
    
    return results