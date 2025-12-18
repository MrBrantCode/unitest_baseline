"""
QUESTION:
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""

def find_kth_lexicographical_number(n: int, k: int) -> int:
    s, nn = 0, str(n)
    while nn:
        if not k:
            return s
        c, m = 0, 10 ** (len(nn) - 1)
        mm, p, t = ((m - 1) // 9, int(nn) // m, 0)
        for i in range(1 if not s else 0, p):
            cc = c + m + mm
            if cc >= k:
                s = 10 * s + i
                k -= c + 1
                nn = '9' * (len(nn) - 1)
                t = 1
                break
            c = cc
        if not t:
            cc = c + int(nn) - m * p + 1 + mm
            if cc >= k:
                s = 10 * s + p
                k -= c + 1
                nn = nn[1:]
            else:
                c = cc
                for i in range(p + 1, 10):
                    cc = c + mm
                    if cc >= k:
                        s = 10 * s + i
                        k -= c + 1
                        nn = '9' * (len(nn) - 2)
                        break
                    c = cc
    return s