"""
QUESTION:
You have $n \times n$ square grid and an integer $k$. Put an integer in each cell while satisfying the conditions below.  All numbers in the grid should be between $1$ and $k$ inclusive.  Minimum number of the $i$-th row is $1$ ($1 \le i \le n$).  Minimum number of the $j$-th column is $1$ ($1 \le j \le n$). 

Find the number of ways to put integers in the grid. Since the answer can be very large, find the answer modulo $(10^{9} + 7)$. [Image] These are the examples of valid and invalid grid when $n=k=2$. 


-----Input-----

The only line contains two integers $n$ and $k$ ($1 \le n \le 250$, $1 \le k \le 10^{9}$).


-----Output-----

Print the answer modulo $(10^{9} + 7)$.


-----Examples-----
Input
2 2

Output
7

Input
123 456789

Output
689974806



-----Note-----

In the first example, following $7$ cases are possible. [Image] 

In the second example, make sure you print the answer modulo $(10^{9} + 7)$.
"""

def count_ways_to_fill_grid(n, k):
    mod = 10**9 + 7
    max_n = 10**4
    
    # Precompute factorials and inverse factorials modulo mod
    fac = [1] + [0] * max_n
    fac_i = [1] + [0] * max_n
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % mod
        fac_i[i] = fac_i[i - 1] * pow(i, mod - 2, mod) % mod

    # Function to compute nCr modulo mod
    def mod_nCr(n, r):
        if n == 0 and r == 0:
            return 1
        if n < r or n < 0:
            return 0
        temp = fac_i[n - r] * fac_i[r] % mod
        return temp * fac[n] % mod

    # Calculate the number of ways to fill the grid
    ans = 0
    for i in range(n + 1):
        base = (pow(k, n - i, mod) * pow(k - 1, i, mod) - pow(k - 1, n, mod) + mod) % mod
        val = pow(-1, i) * mod_nCr(n, i) * pow(base, n, mod) % mod
        ans = (ans + val) % mod
    
    return ans