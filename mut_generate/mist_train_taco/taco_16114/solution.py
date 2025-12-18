"""
QUESTION:
Bob has received a binary string of length N transmitted by Alice. He knows that due to errors in transmission, up to K bits might have been corrupted (and hence flipped). However, he also knows that the string Alice had intended to transmit was not periodic. A string is not periodic if it cannot be represented as a smaller string concatenated some number of times. For example, "0001", "0110" are not periodic while "00000", "010101" are periodic strings.

Now he wonders how many possible strings could Alice have transmitted.

Input Format

The first line contains the number of test cases T. T test cases follow. Each case contains two integers N and K on the first line, and a binary string of length N on the next line.

Constraints

$1\leq T\leq20$ 

$1\leq N\leq1000$ 

$0\leq K\leq N$  

Output Format

Output T lines, one for each test case. Since the answers can be really big, output the numbers modulo 1000000007.

Sample Input 0
3  
5 0  
00000  
3 1  
001  
3 3  
101

Sample Output 0
0
3
6

Explanation 0

Explanation: For the second example, Alice could have transmitted "001", or "011" or "101". 

For the third example, Alice could have transmitted 001, 010, 100, 011, 101, 110
"""

from math import factorial, sqrt

MOD = 1000000007

def nck(n, k):
    res = 0
    for i in range(k + 1):
        res += factorial(n) // (factorial(i) * factorial(n - i))
    return res

def divisors(n):
    d1 = [1]
    d2 = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            d1.append(i)
            if i * i != n:
                d2.append(n // i)
    d1.extend(d2[::-1])
    return d1

def count_possible_strings(N, K, S):
    if N == 1:
        return (N + K) % MOD
    
    total = nck(N, K)
    div = divisors(N)
    dp = [[0] * (N + K + 1) for i in range(len(div))]
    is_periodic = False
    
    for (i, d) in enumerate(div):
        dp[i][0] = 1
        for offset in range(d):
            zeros = 0
            for j in range(offset, N, d):
                if S[j] == '0':
                    zeros += 1
            ones = N // d - zeros
            prev = list(dp[i])
            dp[i][:] = [0] * (N + K + 1)
            for k in range(K + 1):
                if prev[k]:
                    dp[i][k + zeros] += prev[k]
                    dp[i][k + ones] += prev[k]
        if dp[i][0]:
            is_periodic = True
        for i2 in range(i):
            d2 = div[i2]
            if d % d2 == 0:
                for k in range(K + 1):
                    dp[i][k] -= dp[i2][k]
        for k in range(1, K + 1):
            total -= dp[i][k]
    
    return (total - is_periodic) % MOD