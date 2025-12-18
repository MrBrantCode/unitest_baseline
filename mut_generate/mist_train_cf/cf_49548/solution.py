"""
QUESTION:
Calculate the total number of steps B(N) required to arrange N bowls in a non-descending order of beans, where each bowl n initially contains S_n beans and S_n is defined by the sequence S_0 = 290797 and S_n = S_{n-1}^2 mod 50515093 for n > 0. The bowls are arranged by iteratively transferring a single bean from bowl n to bowl n+1 whenever the number of beans in bowl n strictly surpasses the number of beans in bowl n+1. The function should be able to compute B(10^7) efficiently without using excessive memory and computation power.
"""

def entrance(N):
    mod = 50515093
    S_n = 290797
    counter = 0

    for n in range(N):
        S_n = (S_n ** 2) % mod
        counter += max(0, S_n - n)

    return counter