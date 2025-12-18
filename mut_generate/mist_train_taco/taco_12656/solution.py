"""
QUESTION:
Given are N integers A_1,\ldots,A_N.
We will choose exactly K of these elements. Find the maximum possible product of the chosen elements.
Then, print the maximum product modulo (10^9+7), using an integer between 0 and 10^9+6 (inclusive).

-----Constraints-----
 - 1 \leq K \leq N \leq 2\times 10^5
 - |A_i| \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 \ldots A_N

-----Output-----
Print the maximum product modulo (10^9+7), using an integer between 0 and 10^9+6 (inclusive).

-----Sample Input-----
4 2
1 2 -3 -4

-----Sample Output-----
12

The possible products of the two chosen elements are 2, -3, -4, -6, -8, and 12, so the maximum product is 12.
"""

def max_product_modulo(N, K, A):
    MOD = 10**9 + 7
    
    # Separate positive and negative numbers
    s = [x for x in A if x >= 0]
    t = [x for x in A if x < 0]
    
    ok = False
    if len(s) > 0:
        if N == K:
            ok = len(t) % 2 == 0
        else:
            ok = True
    else:
        ok = K % 2 == 0
    
    ans = 1
    if not ok:
        # If we can't get a non-negative product, choose the smallest absolute values
        x = sorted(A, key=lambda x: abs(x))
        for i in range(K):
            ans = ans * x[i] % MOD
    else:
        # Sort the positive and negative numbers appropriately
        s.sort()
        t.sort(key=lambda x: abs(x))
        
        # If K is odd, we need at least one positive number
        if K % 2 == 1:
            ans = ans * s.pop() % MOD
        
        # Create pairs of products
        p = []
        while len(s) >= 2:
            x = s.pop() * s.pop()
            p.append(x)
        while len(t) >= 2:
            x = t.pop() * t.pop()
            p.append(x)
        
        # Sort pairs in descending order
        p.sort(reverse=True)
        
        # Multiply the largest pairs to get the maximum product
        for i in range(K // 2):
            ans = ans * p[i] % MOD
    
    return ans