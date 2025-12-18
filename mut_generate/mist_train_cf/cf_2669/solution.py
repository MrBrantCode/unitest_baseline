"""
QUESTION:
Implement a function called `binomial_coefficient(n, k)` that takes two integers `n` and `k` as input and returns the binomial coefficient `C(n, k)` modulo `10^9+7`. The input integers `n` and `k` must satisfy the condition `k <= n`.
"""

def binomial_coefficient(n, k):
    if k > n/2:
        k = n - k
    
    coefficient = 1
    for i in range(1, k+1):
        coefficient *= n - i + 1
        coefficient //= i
        coefficient %= (10**9 + 7)
    
    return coefficient