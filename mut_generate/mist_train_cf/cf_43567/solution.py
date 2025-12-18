"""
QUESTION:
Write a function `solve()` that determines after how many successful calls, excluding misdials, will 99% of the users (inclusive of the Prime Minister with phone number 524287) be a friend, or a friend of a friend and so forth, of the Prime Minister in a telecommunication system with a user base of one million, where the caller's and the recipient's telephone numbers are represented as Caller(n) = S_{2n-1} and Called(n) = S_{2n} respectively, and S_k is derived from the "Lagged Fibonacci Generator". 

Function `solve()` should take no arguments and return the number of successful calls. The Lagged Fibonacci Generator is defined as: for 1 ≤ k ≤ 55, S_k = [100003 - 200003k + 300007k^3] (mod 1000000), and for 56 ≤ k, S_k = [S_{k-24} + S_{k-55}] (mod 1000000). A call is deemed unsuccessful if Caller(n) = Called(n), indicating a misdial, otherwise it is successful.
"""

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    x_par = find(x, parent)
    y_par = find(y, parent)
    if x_par != y_par:
        parent[y_par] = x_par
        size[x_par] += size[y_par]

def solve():
    n = 10**6
    PM = 524287
    target = n * 0.99
    parent = list(range(n+1)) 
    size = [1] * (n+1)   
    S = [0] * max(56, n+2)  
    for k in range(1, 56):
        S[k] = (100003 - 200003*k + 300007*k**3) % 10**6
    for k in range(56, n+2):
        S[k] = (S[k-24] + S[k-55]) % 10**6
    successful_calls = 0  
    for i in range(1, n+1):
        caller, callee = S[2*i-1], S[2*i]
        if caller != callee:
            successful_calls += 1
            union(caller, callee, parent, size)
            if size[find(PM, parent)] >= target:
                return successful_calls