"""
QUESTION:
Calculate the sum of F_k(N) for all odd k, where F_k(N) is the sum of (A+B) for all pairs (A,B) that can transform any k-gonal number into another k-gonal number and max(A,B) ≤ N. 

The function F_k(N) should be calculated for k-gonal numbers with odd k. The transformation formula is given by AT_n + B = T_{n+1}, where A and B are positive integers. 

The sum should be calculated for all odd k up to a specified limit N, which is given as 10^12.
"""

def entrance(N):
    total_sum = 0
    for k in range(3, N+1, 2):
        total_sum += 2*k*N
    return total_sum