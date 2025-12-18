"""
QUESTION:
Write a function `find_seq(s1, s2, N)` that takes two strings `s1` and `s2`, and an integer `N` as input, and returns the shortest non-reoccurring sequence of characters within the concatenated string `s1 + s2` that has at least `N` distinct characters.
"""

def find_seq(s1, s2, N):
    text = s1 + s2
    n = len(text)
    distinct_chars = dict()
    start = 0
    min_length = float('inf')
    min_seq = ""

    for end in range(n):
        if text[end] in distinct_chars:
            distinct_chars[text[end]] += 1
        else:
            distinct_chars[text[end]] = 1

        while len(distinct_chars) >= N:
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_seq = text[start:end+1]
            distinct_chars[text[start]] -= 1
            if distinct_chars[text[start]] == 0:
                del distinct_chars[text[start]]
            start += 1
    return min_seq