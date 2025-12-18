"""
QUESTION:
Given two positive integers `n` and `k`, find the count of `1`s in the first `k` bits of the binary string `Sn`, where `Sn` is formed by the recursive rule `Si = Si-1 + "1" + reverse(invert(Si-1))` for `i > 1`. 

The function should be named `findKthBitCount` and take two parameters `n` and `k`, where `1 <= n <= 20` and `1 <= k <= 2n - 1`. Return the count of `1`s in the first `k` bits of `Sn`.
"""

def findKthBitCount(n: int, k: int) -> int:
    def findKthBit(n: int, k: int) -> int:
        if n == 1:
            return 0
        l = 2 ** n - 1
        if k == l // 2 + 1:
            return 1
        if k > l // 2:
            return findKthBit(n - 1, l - k + 1) ^ 1
        else:
            return findKthBit(n - 1, k)

    bit_count = 0
    for i in range(1, k + 1):
        bit = findKthBit(n, i)
        bit_count += bit
    return bit_count