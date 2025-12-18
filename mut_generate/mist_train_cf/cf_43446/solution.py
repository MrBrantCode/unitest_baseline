"""
QUESTION:
Implement a function `min_window(s, t)` that finds the smallest possible continuous subsequence in the string `s` that includes all characters present in the string `t`. The function should return this subsequence as a string. If no such subsequence exists, return an empty string. The function takes two parameters: `s` and `t`, both of which are non-empty strings.
"""

def min_window(s, t):
    from collections import Counter

    if not t or not s:
        return ''

    dict_t = Counter(t)
    required = len(dict_t)

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float('inf'), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1    

        r += 1    

    return '' if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]