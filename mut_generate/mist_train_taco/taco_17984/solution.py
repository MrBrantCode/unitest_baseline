"""
QUESTION:
Given are integer sequence of length N, A = (A_1, A_2, \cdots, A_N), and an integer K.
For each X such that 1 \le X \le K, find the following value:
\left(\displaystyle \sum_{L=1}^{N-1} \sum_{R=L+1}^{N} (A_L+A_R)^X\right) \bmod 998244353

-----Constraints-----
 - All values in input are integers.
 -  2 \le N \le 2 \times 10^5
 -  1 \le K \le 300 
 -  1 \le A_i \le 10^8 

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 \cdots A_N

-----Output-----
Print K lines.
The X-th line should contain the value \left(\displaystyle \sum_{L=1}^{N-1} \sum_{R=L+1}^{N} (A_L+A_R)^X \right) \bmod 998244353.

-----Sample Input-----
3 3
1 2 3

-----Sample Output-----
12
50
216

In the 1-st line, we should print (1+2)^1 + (1+3)^1 + (2+3)^1 = 3 + 4 + 5 = 12.
In the 2-nd line, we should print (1+2)^2 + (1+3)^2 + (2+3)^2 = 9 + 16 + 25 = 50.
In the 3-rd line, we should print (1+2)^3 + (1+3)^3 + (2+3)^3 = 27 + 64 + 125 = 216.
"""

import numpy as np

def calculate_sum_of_powers(N, K, A):
    mod = 998244353
    
    # Precompute factorial and inverse factorial modulo mod
    fact = [1] * (K + 1)
    for i in range(1, K + 1):
        fact[i] = i * fact[i - 1] % mod
    inv_fact = [pow(f, mod - 2, mod) for f in fact]
    
    # Initialize result array
    r = [0] * (K + 1)
    r[0] = N
    
    # Compute r[i] for each power i
    temp = np.ones(N, dtype='int32')
    for i in range(1, K + 1):
        temp = temp * A % mod
        r[i] = int(np.sum(temp)) % mod
    
    # Compute inverse of 2 modulo mod
    inv2 = pow(2, mod - 2, mod)
    
    # Compute the final result for each power x
    result = []
    for x in range(1, K + 1):
        ans = sum((fact[x] * inv_fact[t] * inv_fact[x - t] * r[x - t] * r[t] % mod for t in range(x + 1))) % mod
        ans -= r[x] * pow(2, x, mod) % mod
        result.append(ans * inv2 % mod)
    
    return result