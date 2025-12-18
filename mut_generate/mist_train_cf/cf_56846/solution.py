"""
QUESTION:
Given a string `text` and a list of `forbidden` substrings, find the largest possible value of `k` such that `text` can be split into `k` substrings `(subtext1, subtext2, ..., subtextk)` where each `subtexti` is a non-empty string, the concatenation of all substrings is equal to `text`, and `subtexti == subtextk - i + 1` for all valid values of `i`. The substrings cannot contain any of the `forbidden` substrings. Return `k` if such a decomposition is possible, otherwise return 0. The length of `text` is between 1 and 1000, and both `text` and `forbidden` consist only of lowercase English characters.
"""

def longestDecomposition(text, forbidden):
    stack, l, r, sub_l, sub_r = [], 0, len(text) - 1, "", ""
    while l <= r:
        sub_l, sub_r = sub_l + text[l], text[r] + sub_r
        l, r = l + 1, r - 1
        if sub_l == sub_r and sub_l not in forbidden:
            stack.append(sub_l)
            sub_l, sub_r = "", ""
        elif sub_l in forbidden or sub_r in forbidden:
            return 0
    return len(stack)