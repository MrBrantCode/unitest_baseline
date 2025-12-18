"""
QUESTION:
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
 
Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""

 
Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""

def find_longest_duplicate_substring(S: str) -> str:
    nums = [ord(c) - ord('a') for c in S]
    N = len(S)
    BASE, MOD = 26, 2 ** 32

    def check(L: int) -> int:
        cur_hash = 0
        seen = set()
        for val in nums[:L]:
            cur_hash = (cur_hash * BASE + val) % MOD
        seen.add(cur_hash)
        X = pow(BASE, L - 1, MOD)
        for idx, val in enumerate(nums[L:]):
            cur_hash -= nums[idx] * X
            cur_hash = (cur_hash * BASE + val) % MOD
            if cur_hash in seen:
                return idx + 1
            seen.add(cur_hash)
        return -1

    low, high = 1, N + 1
    start = 0
    while low < high:
        mid = (low + high) // 2
        idx = check(mid)
        if idx != -1:
            low = mid + 1
            start = idx
        else:
            high = mid

    return S[start:start + low - 1]