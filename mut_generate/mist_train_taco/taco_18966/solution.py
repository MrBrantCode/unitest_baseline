"""
QUESTION:
Given a positive integer n, find k integers (not necessary distinct) such that all these integers are strictly greater than 1, and their product is equal to n.

Input

The first line contains two integers n and k (2 ≤ n ≤ 100000, 1 ≤ k ≤ 20).

Output

If it's impossible to find the representation of n as a product of k numbers, print -1.

Otherwise, print k integers in any order. Their product must be equal to n. If there are multiple answers, print any of them.

Examples

Input

100000 2


Output

2 50000 


Input

100000 20


Output

-1


Input

1024 5


Output

2 64 2 2 2
"""

from math import sqrt

def find_k_factors(n, k):
    # Helper function to find k factors
    def kfact(n, k, memo):
        if (n, k) in memo:
            return memo[(n, k)]
        if k == 1:
            return [n] if n > 1 else None
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                result = kfact(n // i, k - 1, memo)
                if result:
                    memo[(n, k)] = [i] + result
                    return memo[(n, k)]
        return None
    
    # Memoization dictionary
    memo = {}
    
    # Call the helper function
    result = kfact(n, k, memo)
    
    # Return the result
    return result if result else -1