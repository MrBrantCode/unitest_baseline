"""
QUESTION:
Moamen and Ezzat are playing a game. They create an array $a$ of $n$ non-negative integers where every element is less than $2^k$.

Moamen wins if $a_1 \,\&\, a_2 \,\&\, a_3 \,\&\, \ldots \,\&\, a_n \ge a_1 \oplus a_2 \oplus a_3 \oplus \ldots \oplus a_n$.

Here $\&$ denotes the bitwise AND operation , and $\oplus$ denotes the bitwise XOR operation .

Please calculate the number of winning for Moamen arrays $a$.

As the result may be very large, print the value modulo $1000000\,007$ ($10^9 + 7$).


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 5$)— the number of test cases.

Each test case consists of one line containing two integers $n$ and $k$ ($1 \le n\le 2\cdot 10^5$, $0 \le k \le 2\cdot 10^5$).


-----Output-----

For each test case, print a single value — the number of different arrays that Moamen wins with.

Print the result modulo $1000000\,007$ ($10^9 + 7$).


-----Examples-----

Input
3
3 1
2 1
4 0
Output
5
2
1


-----Note-----

In the first example, $n = 3$, $k = 1$. As a result, all the possible arrays are $[0,0,0]$, $[0,0,1]$, $[0,1,0]$, $[1,0,0]$, $[1,1,0]$, $[0,1,1]$, $[1,0,1]$, and $[1,1,1]$.

Moamen wins in only $5$ of them: $[0,0,0]$, $[1,1,0]$, $[0,1,1]$, $[1,0,1]$, and $[1,1,1]$.
"""

def calculate_winning_arrays(t, test_cases):
    pri = 1000000007
    results = []
    
    for n, k in test_cases:
        g1 = pow(2, n, pri)
        g2 = pow(2, n, pri)
        
        if k == 0:
            results.append(1)
            continue
        
        ans = [0] * k
        
        if n % 2 == 0:
            ways = pow(2, n - 1, pri)
        else:
            ways = pow(2, n - 1, pri) + 1
        
        ans[0] = ways % pri
        
        for i in range(1, k):
            if n % 2 == 0:
                ways = pow(2, n - 1, pri)
            else:
                ways = pow(2, n - 1, pri) + 1
            
            ways %= pri
            
            if n % 2 == 0:
                ans[i] = ans[i - 1] * (ways - 1) % pri
                ans[i] += g2
                ans[i] %= pri
                g2 = g2 * g1 % pri
            else:
                ans[i] = ans[i - 1] * ways % pri
        
        results.append(ans[-1])
    
    return results