"""
QUESTION:
Determine the value of G(500) where G(n) = ∑[g(s+p+q,s,p,q)] for s+p+q ≤ n, p < q, p ≥ 5, s ≥ 5, and all s, p, q are integers. The function g(c,s,p,q) represents the number of gear arrangements for given values of c, s, p, q, where c, s, p, q are the circumferences of circles C, S, P, Q respectively.
"""

def G(n):
    """
    Calculate the value of G(n) for given n.

    G(n) is the sum of g(s+p+q,s,p,q) for s+p+q ≤ n, p < q, p ≥ 5, s ≥ 5, 
    and all s, p, q are integers.

    Args:
    n (int): The upper limit for the sum.

    Returns:
    int: The value of G(n).
    """
    count = 0
    for s in range(5, n+1):
        for p in range(5, s+1):
            for q in range(p+1, n-s-p+1):
                if s*s + 2*s*(p + q) <= (s + p + q)*(s + p + q):
                    count += 1
    return count