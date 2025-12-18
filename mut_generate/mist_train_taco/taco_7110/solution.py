"""
QUESTION:
A message containing letters from A-Z is being encoded to numbers using the following mapping:


'A' -> 1
'B' -> 2
...
'Z' -> 26


Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:


Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).


Example 2:


Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

def decode_ways(s: str) -> int:
    if not s:
        return 0

    def num_decode(i: int) -> int:
        if i == len(s):
            return 1
        if i not in memo:
            num_ways = 0
            if s[i] in single_digit_codes:
                num_ways += num_decode(i + 1)
            if i + 1 < len(s) and s[i:i + 2] in double_digit_codes:
                num_ways += num_decode(i + 2)
            memo[i] = num_ways
        return memo[i]

    single_digit_codes = set((str(x) for x in range(1, 10)))
    double_digit_codes = set((str(x) for x in range(10, 27)))
    memo = {}
    return num_decode(0)