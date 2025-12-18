"""
QUESTION:
Define a function `maxRepetitions(s1, n1, s2, n2)` that takes two non-empty strings `s1` and `s2` (each at most 100 characters long) and two integers `0 ≤ n1 ≤ 10^6` and `1 ≤ n2 ≤ 10^6` as input. The function should return the maximum integer `M` such that `[s2, M]` can be obtained from `[s1, n1]` by removing some characters from `[s1, n1]`.
"""

def maxRepetitions(s1, n1, s2, n2):
    len1 = len(s1)
    len2 = len(s2)
    start = [0] * len2
    count = [0] * len2
    j = 0
    cnt = 0
    for k in range(1, n1 + 1):
        for i in range(len1):
            if s1[i] == s2[j]:
                j += 1
                if j == len2:
                    j = 0
                    cnt += 1
        start[k % len2] = j
        count[k % len2] = cnt
        if k > 1 and start[k % len2] == start[(k - 1) % len2]:
            prefix_cnt = count[(k - 1) % len2]
            loop_cnt = (cnt - count[(k - 1) % len2]) * ((n1 - (k - 1)) // (k - (k - 1)))
            suffix_cnt = count[(k - 1) % len2 + ((n1 - (k - 1)) % (k - (k - 1)))]
            return (prefix_cnt + loop_cnt + suffix_cnt) // n2
    return cnt // n2