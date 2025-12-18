"""
QUESTION:
Write two functions: `longest_common_substring(s, t, n)` and `common_substrings(s, t, n)`.

Function `longest_common_substring(s, t, n)` should take two text strings `s` and `t`, and an integer `n` as input. It should return the maximal length of the identical substring sequence shared by `s` and `t` that is not less than `n` characters. If such a sequence doesn't exist, it should return -1.

Function `common_substrings(s, t, n)` should take two text strings `s` and `t`, and an integer `n` as input. It should return all unique substring sequences of length `n` that exist in both `s` and `t`. 

The function should not print anything; it should only return the result.
"""

def longest_common_substring(s, t, n):
    max_length = 0
    for length in range(n, min(len(s), len(t)) + 1):
        s_subs = {s[i: i + length] for i in range(len(s) - length + 1)}
        t_subs = {t[i: i + length] for i in range(len(t) - length + 1)}
        common = s_subs.intersection(t_subs)
        if common:
            max_length = length
        else:
            break
    return max_length if max_length >= n else -1

def common_substrings(s, t, n):
    s_subs = {s[i: i + n] for i in range(len(s) - n + 1)}
    t_subs = {t[i: i + n] for i in range(len(t) - n + 1)}
    common = s_subs.intersection(t_subs)
    return common