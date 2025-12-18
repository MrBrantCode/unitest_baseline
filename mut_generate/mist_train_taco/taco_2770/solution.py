"""
QUESTION:
You are given an array A = [1, 2, 3, ..., n]:     

How many sequences ($S_{1}$) can you get after exact k adjacent swaps on A? 

How many sequences ($S_{2}$) can you get after at most k swaps on A?  

An adjacent swap can be made between two elements of the Array A, A[i] and A[i+1] or A[i] and A[i-1]. 

A swap otherwise can be between any two elements of the array A[i] and A[j] ∀ 1 ≤ i, j ≤ N, i ≠ j.

Input Format

First and only line contains n and k separated by space.    

Constraints

1 ≤ n ≤ 2500 

1 ≤ k ≤ 2500      

Output Format

Output $S_{1}$ % MOD and $S_{2} $% MOD in one line, where MOD = 1000000007.    

Sample Input
3 2

Sample Output
3 6

Explanation
Original array: [1, 2, 3]
1. After 2 adjacent swaps:
We can get [1, 2, 3], [2, 3, 1], [3, 1, 2] ==> S1 == 3

2. After at most 2 swaps:
1) After 0 swap: [1, 2, 3]
2) After 1 swap: [2, 1, 3], [3, 2, 1], [1, 3, 2].
3) After 2 swaps: [1, 2, 3], [2, 3, 1], [3, 1, 2]
==> S2 == 6
"""

from itertools import accumulate, chain, islice

MOD = 1000000007

def calculate_sequences(n, k):
    def adjswap(n, k):
        if n == 1:
            return int(k == 0)
        permcount = [1] * (k + 1)
        for nperm in range(3, n + 1):
            oldpermcount = permcount
            cumsum = list(accumulate(oldpermcount))
            permcount = chain(islice(cumsum, nperm), (a - b for (a, b) in zip(islice(cumsum, nperm, None), cumsum)))
            permcount = [x % MOD for x in permcount]
        return permcount[-1]

    def anyswap(n, k):
        arr = [1] * (k + 1)
        for i in range(n):
            arr = [(a + i * b) % MOD for (a, b) in zip(arr, [0] + arr[:-1])]
        return arr[-1]

    s1 = adjswap(n, k)
    s2 = anyswap(n, k)
    
    return s1, s2