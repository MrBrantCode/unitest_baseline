"""
QUESTION:
You are given an even integer `n`, a multiple of 3, where `3 <= n <= 1000`. You need to find the minimum non-zero number of operations to return a permutation of size `n` to its initial state, where the permutation is transformed according to the following rules: 
- If `i % 3 == 0`, then `arr[i] = perm[i / 3]`.
- If `i % 3 == 1`, then `arr[i] = perm[n / 3 + (i - 1) / 3]`.
- If `i % 3 == 2`, then `arr[i] = perm[2 * n / 3 + (i - 2) / 3]`. 
Implement the function `reinitialize(n)`.
"""

def reinitializePermutation(n):
    perm = list(range(n))
    arr = perm.copy()
    ops = 0
    while True:
        ops += 1
        for i in range(n):
            if i % 3 == 0:
                arr[i] = perm[i // 3]
            elif i % 3 == 1:
                arr[i] = perm[n // 3 + (i - 1) // 3]
            else:
                arr[i] = perm[2 * n // 3 + (i - 2) // 3]
        if arr == list(range(n)):
            return ops
        perm = arr.copy()