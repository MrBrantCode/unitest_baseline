"""
QUESTION:
Write a function R(M, N) that calculates the number of ways to cut an M x N rectangle with integer dimensions, following the rules that cuts can only be made between two points lying on different sides of the rectangle and having integer coordinates, and two cuts cannot cross. The function should return the result modulo 10^8. The input M and N are positive integers.
"""

MOD = 10**8

memo = { (1,1): 2 }

def R(M, N):
    return R_helper((M, N))

def R_helper(sizes):
    if sizes in memo:
        return memo[sizes]
    res = 0
    for i in range(len(sizes)):
        for j in range(i):
            newSizes = list(sizes)
            m, n = newSizes.pop(i), newSizes.pop(j)
            for split in range(1, m):
                for cut in range(1, n):
                    newSizes.append(m + n - split - cut)
                    newSizes.sort()
                    res += R_helper(tuple(newSizes))
                    newSizes.pop()
            res %= MOD
    memo[sizes] = res
    return res