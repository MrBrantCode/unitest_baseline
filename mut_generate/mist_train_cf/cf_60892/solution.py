"""
QUESTION:
Function F(K, X) should be defined to calculate the count of integer quadruplets (k, a, b, c) that satisfy the following conditions: 
1) The points A(a, a^2/k), B(b, b^2/k), and C(c, c^2/k) form a triangle with at least one angle of 45 degrees.
2) The constraints 1 ≤ k ≤ K and -X ≤ a < b < c ≤ X hold.
Note that F(1, 10) = 41 and F(10, 100) = 12492.
"""

def F(K, X):
    res = 0
    for a in range(-X, X+1):
        for k in range(1, K+1):
            b = 3*a
            if a<b and b<=X:
                res += 2
    return res