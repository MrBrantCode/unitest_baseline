"""
QUESTION:
Given two positive integers `n` and `k`, determine the `kth` bit in the `n`-th binary string `Sn`, which is constructed as follows:
- `S1 = "0"`
- `Si = Si-1 + "1" + reverse(invert(Si-1))` for `i > 1`

Return the `kth` bit in `Sn`.

Restrictions:
- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`
- `k` is a valid value for the provided `n`
"""

def find_kth_bit(n, k):
    length = 2 ** n - 1
    if n == 1:
        return "0"
    if k == length // 2 + 1:
        return "1"
    if k > length // 2:
        return "1" if find_kth_bit(n - 1, length - k + 1) == "0" else "0"
    return find_kth_bit(n - 1, k)