"""
QUESTION:
Write a function `count_matches(N, S, l)` that determines the number of times a cyclist's position matches a specified segment `S` after traversing an entire circular track with `N` segments. The function takes three parameters: `N`, an integer representing the number of segments (2 <= N <= 10^5); `S`, an integer representing the specified segment (0 <= S <= N-1); and `l`, a list of `N` integers representing the lengths of the segments (1 <= l[i] <= 1000).
"""

def count_matches(N, S, lengths):
    c = 0
    S -= 1  # Adjust S to 0-based index
    ans = 0
    for i in lengths:
        ans += c == S
        c = (c + i + N) % N  # Update cyclist's position
    ans += c == S
    return ans