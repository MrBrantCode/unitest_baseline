"""
QUESTION:
Find the number of k-divisible numbers on the segment [a, b]. In other words you need to find the number of such integer values x that a ≤ x ≤ b and x is divisible by k.


-----Input-----

The only line contains three space-separated integers k, a and b (1 ≤ k ≤ 10^18; - 10^18 ≤ a ≤ b ≤ 10^18).


-----Output-----

Print the required number.


-----Examples-----
Input
1 1 10

Output
10

Input
2 -4 4

Output
5
"""

def count_k_divisible_in_range(k, a, b):
    def solver(n, k):
        return n // k
    
    if k == 1:
        return b - a + 1
    elif a == 0:
        return solver(b, k) + 1
    elif a > 0:
        return solver(b, k) - solver(a - 1, k)
    else:
        return solver(b, k) + solver(-a, k) + 1