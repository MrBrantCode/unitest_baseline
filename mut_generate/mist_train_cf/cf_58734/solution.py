"""
QUESTION:
Develop a function named `shortest_substring(s)` that locates and extracts the shortest substring containing all distinct characters in a given string `s`. The function should return the shortest substring and its start and end indices in the original string. The function should work under the constraint that the input string `s` only contains ASCII characters.
"""

def shortest_substring(s):
    n_distinct_chars = len(set(s))
    n_chars = len(s)
    start, end = 0, 0
    min_len = float('inf')
    min_start, min_end = 0, 0
    count = [0] * 256
    distinct_chars = 0

    while end < n_chars:
        count[ord(s[end])] += 1
        if count[ord(s[end])] == 1:
            distinct_chars += 1
        if distinct_chars == n_distinct_chars:
            while count[ord(s[start])] > 1:
                count[ord(s[start])] -= 1
                start += 1
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_start, min_end = start, end
        end += 1
    return s[min_start:min_end+1], min_start, min_end