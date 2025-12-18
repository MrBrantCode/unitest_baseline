"""
QUESTION:
How many strings can be obtained by applying the following operation on a string S exactly K times: "choose one lowercase English letter and insert it somewhere"?
The answer can be enormous, so print it modulo (10^9+7).

-----Constraints-----
 - K is an integer between 1 and 10^6 (inclusive).
 - S is a string of length between 1 and 10^6 (inclusive) consisting of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
K
S

-----Output-----
Print the number of strings satisfying the condition, modulo (10^9+7).

-----Sample Input-----
5
oof

-----Sample Output-----
575111451

For example, we can obtain proofend, moonwolf, and onionpuf, while we cannot obtain oofsix, oofelevennn, voxafolt, or fooooooo.
"""

def count_strings_after_operations(K: int, S: str) -> int:
    """
    Calculate the number of distinct strings that can be obtained by inserting 
    exactly K lowercase English letters into the string S, modulo 10^9 + 7.

    Parameters:
    K (int): The number of operations (insertions) to perform.
    S (str): The initial string consisting of lowercase English letters.

    Returns:
    int: The number of distinct strings modulo 10^9 + 7.
    """
    from functools import reduce

    MOD = 10 ** 9 + 7

    def comb(n, max_k, mod):
        res = [1] * (max_k + 1)
        t = 1
        for i in range(max_k + 1):
            res[i] *= t
            t *= n - i
            t %= mod
        n = reduce(lambda x, y: x * y % mod, range(1, max_k + 1), 1)
        n = pow(n, -1, mod)
        for i in reversed(range(max_k + 1)):
            res[i] *= n
            res[i] %= mod
            n *= i
            n %= mod
        return res

    N = len(S)
    res = 0
    x = 1
    com = comb(N + K, K, MOD)
    for c in com:
        res += x * c
        res %= MOD
        x *= 25
        x %= MOD
    return res