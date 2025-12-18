"""
QUESTION:
Let us calculate the sum of k-th powers of natural numbers from 1 to n. As the result can be quite large, output the result modulo some integer p.

------ Input ------ 

First t≤10 - the number of test cases.
Each test case consist of numbers: 1≤n≤1000000000, 1≤k≤100, 1≤p≤1000000000.

------ Output ------ 

For each test case, output the value: (1^{k}+2^{k}+...+n^{k}) mod p.

----- Sample Input 1 ------ 
4
10 1 1000000
10 2 1000000
10 3 1000000
10 4 1000000
----- Sample Output 1 ------ 
55
385
3025
25333
"""

def sum_of_powers_modulo(n: int, k: int, p: int) -> int:
    r = 10 ** 2 + 5
    d = [0] * (10 ** 5)
    s = [0] * r
    
    # Initialize the d array
    for j in range(r):
        for k_inner in range(r):
            if j == k_inner or k_inner == 0:
                d[j * r + k_inner] = 1
            else:
                d[j * r + k_inner] = d[(j - 1) * r + k_inner - 1] + d[(j - 1) * r + k_inner]
    
    # Calculate the s array
    for j in range(k + 1):
        ans = pow(n + 1, j + 1) - 1
        for k_inner in range(j):
            ans -= d[(j + 1) * r + k_inner] * s[k_inner]
        s[j] = ans // (j + 1)
    
    # Return the result modulo p
    return s[k] % p